# gemini-2.0-flash-lite
uv run ../openai/query_openai.py ../../../data/source/dashboard_query_list.csv google gemini-2.0-flash-lite ../../../data/intermediate/raw_responses/google/gemini-2.0-flash-lite

uv run parse_google.py google gemini-2.0-flash-lite ../../../data/intermediate/raw_responses/google/gemini-2.0-flash-lite ../../../data/intermediate/parsed_responses/google/gemini-2.0-flash-lite.parquet

# gemini-2.0-flash
uv run ../openai/query_openai.py ../../../data/source/dashboard_query_list.csv google gemini-2.0-flash ../../../data/intermediate/raw_responses/google/gemini-2.0-flash

uv run parse_google.py google gemini-2.0-flash ../../../data/intermediate/raw_responses/google/gemini-2.0-flash ../../../data/intermediate/parsed_responses/google/gemini-2.0-flash.parquet
