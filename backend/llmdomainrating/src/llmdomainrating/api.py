from openai import OpenAI
from llmdomainrating.prompts import (
    SYS_BASE,
    USER_INSTRUCTION,
    DOMAIN_RATING_JSON_SCHEMA,
)


class OpenAIClient:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def response_api(self, domain: str, model: str):
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
