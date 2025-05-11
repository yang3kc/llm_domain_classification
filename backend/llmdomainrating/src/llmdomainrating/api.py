import os
from dotenv import load_dotenv

from openai import OpenAI
from anthropic import Anthropic

from llmdomainrating.prompts import (
    SYS_BASE,
    USER_INSTRUCTION,
    USER_FORMAT,
    DOMAIN_RATING_JSON_SCHEMA,
)


class BaseClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self._create_api_client()

    def _create_api_client(self):
        raise NotImplementedError("Subclasses must implement this method")

    def query_model(self, domain: str, model: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")


class OpenAIClient(BaseClient):
    def __init__(self, api_key: str = None):
        if api_key is None:
            load_dotenv()
            api_key = os.getenv("OPENAI_API_KEY")
        super().__init__(api_key)

    def _create_api_client(self):
        self.client = OpenAI(api_key=self.api_key)

    def query_model(self, domain: str, model: str) -> str:
        if model.startswith("o"):
            resp = self.response_api_reasoning(domain, model)
        else:
            resp = self.response_api(domain, model)
        return resp

    def response_api(self, domain: str, model: str) -> str:
        try:
            resp = self.client.responses.parse(
                model=model,
                instructions=SYS_BASE,
                input=USER_INSTRUCTION.format(domain=domain),
                temperature=0,
                text={
                    "format": {
                        "type": "json_schema",
                        "name": "domain_rating",
                        "strict": True,
                        "schema": DOMAIN_RATING_JSON_SCHEMA,
                    }
                },
            )
            return resp.model_dump_json()
        except Exception as e:
            print(f"Error: {e}")
            return None

    def response_api_reasoning(self, domain: str, model: str) -> str:
        try:
            resp = self.client.responses.parse(
                model=model,
                instructions=SYS_BASE,
                input=USER_INSTRUCTION.format(domain=domain),
                reasoning={
                    "effort": "medium",
                    "summary": "auto",
                },
            )
            return resp.model_dump_json()
        except Exception as e:
            print(f"Error: {e}")
            return None


class AnthropicClient(BaseClient):
    def __init__(self, api_key: str = None):
        if api_key is None:
            load_dotenv()
            api_key = os.getenv("ANTHROPIC_API_KEY")
        super().__init__(api_key)

    def _create_api_client(self):
        self.client = Anthropic(api_key=self.api_key)

    def query_model(self, domain: str, model: str) -> str:
        try:
            resp = self.client.messages.create(
                model=model,
                system=SYS_BASE,
                messages=[
                    {
                        "role": "user",
                        "content": f"{USER_INSTRUCTION.format(domain=domain)}\n{USER_FORMAT}",
                    }
                ],
                max_tokens=8192,
                temperature=0,
            )
            return resp.to_json()
        except Exception as e:
            print(f"Error: {e}")
            return None


def create_api_client(provider: str, api_key: str = None):
    provider_mapping = {
        "openai": OpenAIClient,
        "anthropic": AnthropicClient,
    }
    if provider not in provider_mapping:
        raise ValueError(
            f"Unknown provider: {provider}, must be one of {provider_mapping.keys()}"
        )
    return provider_mapping[provider](api_key)
