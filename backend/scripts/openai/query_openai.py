from llmdomainrating import *

client = create_api_client("openai")

resp = client.response_api("tampabay.com", "gpt-4o-mini")

with open("tampabay.json", "w") as f:
    f.write(resp)
