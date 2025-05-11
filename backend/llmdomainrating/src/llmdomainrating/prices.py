import json

model_prices = {
    "OpenAI": {
        "gpt-4.1-nano-2025-04-14": {"input": 0.1, "output": 0.4, "cached_input": 0.025},
        "gpt-4.1-mini-2025-04-14": {"input": 0.4, "output": 1.6, "cached_input": 0.10},
    }
}


class CostCalculatorBase:
    def __init__(self, model_unit_prices: dict):
        self.model_unit_prices = model_unit_prices

    def calculate_cost(self, response: str) -> dict:
        price_unit = 1_000_000
        token_count = self._extract_token_count(response)
        cost = 0
        for item, num in token_count.items():
            cost += self.model_unit_prices.get(item, 0) * num / price_unit
        return {"cost": cost, "token_count": token_count}

    def _extract_token_count(self, response: str) -> dict:
        raise NotImplementedError("Subclasses must implement this method")


class OpenAICostCalculator(CostCalculatorBase):
    def __init__(self, model_name: str):
        if model_name not in model_prices["OpenAI"]:
            raise ValueError(f"Model {model_name} not found in OpenAI model prices")
        model_unit_prices = model_prices["OpenAI"][model_name]
        super().__init__(model_unit_prices)

    def _extract_token_count(self, response) -> dict:
        if isinstance(response, str):
            with open(response, "r") as f:
                data = json.load(f)
        elif isinstance(response, dict):
            data = response
        else:
            raise ValueError("Invalid response type")
        usage = data["usage"]
        token_count = {
            "input": usage["input_tokens"],
            "cached_input": usage["input_tokens_details"]["cached_tokens"],
            "output": usage["output_tokens"],
            "reasoning_tokens": usage["output_tokens_details"]["reasoning_tokens"],
        }
        return token_count
