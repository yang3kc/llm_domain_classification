import os
import sys
import json
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from tqdm import tqdm


class DomainRatingExtracted(BaseModel):
    rating: float = Field(
        description="Domain credibility rating, ranging from -1 to 1",
    )
    explanation: str = Field(description="Explanation of the rating.")


def load_old_resp_text(file_path):
    with open(file_path, "r") as f:
        resp = json.load(f)
    for item in resp["output"]:
        if item["type"] == "message" and item["role"] == "assistant":
            resp_text = item["content"][0]["text"]
            return resp_text
    return None


def query_openai(resp_text, client, model="gpt-4.1-mini"):
    resp = client.responses.parse(
        model=model,
        instructions="""
            Extract structured information from the provided text. Specifically, identify the rating, which is a number between -1 and 1, and the accompanying explanation. Present this data as a JSON object.

            # Steps

            1. **Identify the Rating**: Scan the text to locate a numerical value that represents the rating, ensure it's within the range of -1 to 1. The rating typically appears at the beginning of the input.
            2. **Extract Explanation**: Find the part of the text that provides context or reasoning for the rating.
            3. **Compile JSON**: Format the rating and explanation into a JSON object.
            """,
        input=resp_text,
        temperature=0,
        text_format=DomainRatingExtracted,
    )
    return resp.model_dump_json()


if __name__ == "__main__":
    load_dotenv()

    raw_data_dir = sys.argv[1]
    output_dir = sys.argv[2]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    client = OpenAI()

    for file in tqdm(os.listdir(raw_data_dir)):
        resp_text_old = load_old_resp_text(os.path.join(raw_data_dir, file))
        if resp_text_old is None:
            print(f"No old response found for {file}")
            continue
        new_resp = query_openai(resp_text_old, client)
        with open(os.path.join(output_dir, file), "w") as f:
            f.write(new_resp)
