# meta-llama/Llama-3.3-70B-Instruct-Turbo
uv run ../openai/query_openai.py ../../../data/source/dashboard_query_list.csv together meta-llama/Llama-3.3-70B-Instruct-Turbo ../../../data/intermediate/raw_responses/together/Llama-3.3-70B-Instruct-Turbo

uv run parse_together.py together Llama-3.3-70B-Instruct-Turbo ../../../data/intermediate/raw_responses/together/Llama-3.3-70B-Instruct-Turbo ../../../data/intermediate/parsed_responses/together/Llama-3.3-70B-Instruct-Turbo.parquet

# meta-llama/Llama-4-Scout-17B-16E-Instruct
uv run ../openai/query_openai.py ../../../data/source/dashboard_query_list.csv together meta-llama/Llama-4-Scout-17B-16E-Instruct ../../../data/intermediate/raw_responses/together/Llama-4-Scout-17B-16E-Instruct

uv run parse_together.py together Llama-4-Scout-17B-16E-Instruct ../../../data/intermediate/raw_responses/together/Llama-4-Scout-17B-16E-Instruct ../../../data/intermediate/parsed_responses/together/Llama-4-Scout-17B-16E-Instruct.parquet

# meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8
uv run ../openai/query_openai.py ../../../data/source/dashboard_query_list.csv together meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 ../../../data/intermediate/raw_responses/together/Llama-4-Maverick-17B-128E-Instruct-FP8

uv run parse_together.py together Llama-4-Maverick-17B-128E-Instruct-FP8 ../../../data/intermediate/raw_responses/together/Llama-4-Maverick-17B-128E-Instruct-FP8 ../../../data/intermediate/parsed_responses/together/Llama-4-Maverick-17B-128E-Instruct-FP8.parquet

# deepseek-ai/DeepSeek-V3
uv run ../openai/query_openai.py ../../../data/source/dashboard_query_list.csv together deepseek-ai/DeepSeek-V3 ../../../data/intermediate/raw_responses/together/DeepSeek-V3

uv run parse_together.py together DeepSeek-V3 ../../../data/intermediate/raw_responses/together/DeepSeek-V3 ../../../data/intermediate/parsed_responses/together/DeepSeek-V3.parquet

# deepseek-ai/DeepSeek-R1
uv run ../openai/query_openai.py ../../../data/source/dashboard_query_list.csv together deepseek-ai/DeepSeek-R1 ../../../data/intermediate/raw_responses/together/DeepSeek-R1

uv run parse_together.py together DeepSeek-R1 ../../../data/intermediate/raw_responses/together/DeepSeek-R1 ../../../data/intermediate/parsed_responses/together/DeepSeek-R1.parquet
