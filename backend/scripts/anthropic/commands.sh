# Claude 3.5 Haiku
uv run ../openai/query_openai.py ../../../data/source/dashboard_query_list.csv anthropic claude-3-5-haiku-20241022 ../../../data/intermediate/raw_responses/anthropic/claude-3-5-haiku-20241022

uv run parse_anthropic.py anthropic claude-3-5-haiku-20241022 ../../../data/intermediate/raw_responses/anthropic/claude-3-5-haiku-20241022 ../../../data/intermediate/parsed_responses/anthropic/claude-3-5-haiku-20241022.parquet

# Claude 3.5 Sonnet
uv run ../openai/query_openai.py ../../../data/source/dashboard_query_list.csv anthropic claude-3-5-sonnet-20241022 ../../../data/intermediate/raw_responses/anthropic/claude-3-5-sonnet-20241022

uv run parse_anthropic.py anthropic claude-3-5-sonnet-20241022 ../../../data/intermediate/raw_responses/anthropic/claude-3-5-sonnet-20241022 ../../../data/intermediate/parsed_responses/anthropic/claude-3-5-sonnet-20241022.parquet
