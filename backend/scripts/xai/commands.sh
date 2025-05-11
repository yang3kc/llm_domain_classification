# Grok3 mini beta
uv run ../openai/query_openai.py ../../../data/source/dashboard_query_list.csv xai grok-3-mini-beta ../../../data/intermediate/raw_responses/xai/grok-3-mini-beta

uv run parse_xai.py xai grok-3-mini-beta ../../../data/intermediate/raw_responses/xai/grok-3-mini-beta ../../../data/intermediate/parsed_responses/xai/grok-3-mini-beta.parquet

# Grok3 beta
uv run ../openai/query_openai.py ../../../data/source/dashboard_query_list.csv xai grok-3-beta ../../../data/intermediate/raw_responses/xai/grok-3-beta

uv run parse_xai.py xai grok-3-beta ../../../data/intermediate/raw_responses/xai/grok-3-beta ../../../data/intermediate/parsed_responses/xai/grok-3-beta.parquet
