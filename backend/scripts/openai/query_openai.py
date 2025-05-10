from llmdomainrating import *

client = OpenAIClient()

resp = client.response_api("tampabay.com", "gpt-4o-mini")

with open("tampabay.json", "w") as f:
    f.write(resp)
