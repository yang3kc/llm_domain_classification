from llmdomainrating import DomainRating, AnthropicCostCalculator
import os
import sys
import pandas as pd
import json
from json_repair import repair_json

provider = sys.argv[1]
model = sys.argv[2]
resp_path = sys.argv[3]
output_path = sys.argv[-1]

cost_calculator = AnthropicCostCalculator(model)

rating_dict_list = []
for file_name in os.listdir(resp_path):
    if file_name.endswith(".txt"):
        domain = file_name[:-4]
        with open(os.path.join(resp_path, file_name), "r") as f:
            resp_json = json.load(f)
            try:
                resp_text = resp_json["content"][0]["text"]
                if resp_text.startswith("```json"):
                    resp_text = repair_json(resp_text)
                rating_obj = DomainRating.model_validate_json(resp_text)
                rating_dict = rating_obj.model_dump()
                rating_dict["domain"] = domain

                cost_dict = cost_calculator.calculate_cost(resp_json)
                rating_dict["cost"] = cost_dict["cost"]
                rating_dict["input_token_count"] = cost_dict["token_count"]["input"]
                rating_dict["output_token_count"] = cost_dict["token_count"]["output"]
                rating_dict["cache_write_token_count"] = cost_dict["token_count"][
                    "cache_write"
                ]
                rating_dict["cache_read_token_count"] = cost_dict["token_count"][
                    "cache_read"
                ]

                rating_dict_list.append(rating_dict)
            except Exception as e:
                print(f"Error parsing {file_name}: {e}")
                continue
rating_df = pd.DataFrame(rating_dict_list)
rating_df["provider"] = provider
rating_df["model"] = model
rating_df.to_parquet(output_path, index=False)

invalid_resp_df = rating_df.query("rating < 0 or rating > 1")
valid_resp_df = rating_df.query("0 <= rating <= 1")
print(f"invalid_resp_df: {invalid_resp_df.shape}")
print(f"valid_resp_df: {valid_resp_df.shape}")
print(f"{len(invalid_resp_df) / len(rating_df) * 100:.2f}% of responses are invalid")
print(f"cost_total: {rating_df.cost.sum():.3f} USD")
