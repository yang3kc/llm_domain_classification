# GPT-4o-mini, for testing purposes
uv run query_openai.py ../../../data/source/dashboard_query_list.csv openai gpt-4o-mini ../../../data/intermediate/raw_responses/openai/gpt4omini

uv run parse_openai.py openai gpt-4o-mini ../../../data/intermediate/raw_responses/openai/gpt4omini ../../../data/intermediate/parsed_responses/openai/gpt4omini.parquet