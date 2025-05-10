from llmdomainrating import *

openai_api_key = load_api_key("../../../api_keys.json", "openai")

client = OpenAIClient(openai_api_key)

resp = client.response_api("tampabay.com", "gpt-4o-mini")

with open("tampabay.json", "w") as f:
    f.write(resp)
