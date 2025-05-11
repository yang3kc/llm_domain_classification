# OpenAI
uv run gen_stats.py ../../../data/intermediate/parsed_responses/openai/gpt-4.1-nano-2025-04-14.parquet gpt-4.1-nano-2025-04-14 OpenAI

uv run gen_stats.py ../../../data/intermediate/parsed_responses/openai/gpt-4.1-mini-2025-04-14.parquet gpt-4.1-mini-2025-04-14 OpenAI

uv run gen_stats.py ../../../data/intermediate/parsed_responses/openai/gpt-4.1-2025-04-14.parquet gpt-4.1-2025-04-14 OpenAI

# Anthropic
uv run gen_stats.py ../../../data/intermediate/parsed_responses/anthropic/claude-3-5-haiku-20241022.parquet claude-3-5-haiku-20241022 Anthropic

uv run gen_stats.py ../../../data/intermediate/parsed_responses/anthropic/claude-3-5-sonnet-20241022.parquet claude-3-5-sonnet-20241022 Anthropic

uv run gen_stats.py ../../../data/intermediate/parsed_responses/anthropic/claude-3-7-sonnet-20250219.parquet claude-3-7-sonnet-20250219 Anthropic

# XAI
uv run gen_stats.py ../../../data/intermediate/parsed_responses/xai/grok-3-beta.parquet grok-3-beta XAI

uv run gen_stats.py ../../../data/intermediate/parsed_responses/xai/grok-3-mini-beta.parquet grok-3-mini-beta XAI

# Together
uv run gen_stats.py ../../../data/intermediate/parsed_responses/together/Llama-3.3-70B-Instruct-Turbo.parquet Llama-3.3-70B-Instruct-Turbo Meta

uv run gen_stats.py ../../../data/intermediate/parsed_responses/together/Llama-4-Scout-17B-16E-Instruct.parquet Llama-4-Scout-17B-16E-Instruct Meta

uv run gen_stats.py ../../../data/intermediate/parsed_responses/together/Llama-4-Maverick-17B-128E-Instruct-FP8.parquet Llama-4-Maverick-17B-128E-Instruct-FP8 Meta

uv run gen_stats.py ../../../data/intermediate/parsed_responses/together/DeepSeek-V3.parquet DeepSeek-V3 DeepSeek

uv run gen_stats.py ../../../data/intermediate/parsed_responses/together/DeepSeek-R1.parquet DeepSeek-R1 DeepSeek
