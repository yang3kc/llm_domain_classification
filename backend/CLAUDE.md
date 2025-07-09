# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with the backend code in this repository.

## Overview

Python backend system for querying multiple LLM providers (OpenAI, Anthropic, Google, XAI, Together) to evaluate domain credibility ratings. Uses a custom `llmdomainrating` package for unified API access and cost calculation.

## Development Setup

```bash
cd backend
uv sync                                    # Install dependencies
uv add --editable ./llmdomainrating/      # Install local package in editable mode
```

## Tech Stack

- **Python 3.12+**: Required minimum version
- **uv**: Package manager and dependency resolver
- **Pydantic**: Data validation and JSON schema generation
- **pandas**: Data manipulation and analysis
- **pyarrow**: Parquet file handling
- **Provider SDKs**: OpenAI, Anthropic, Google GenAI, Together, XAI (via OpenAI SDK)
- **Jupyter**: Notebooks for exploration and analysis

## Architecture

### Core Package Structure (`llmdomainrating/`)
```
llmdomainrating/
├── __init__.py          # Package exports
├── api.py               # Unified API clients for all providers
├── prompts.py           # Standardized prompts and JSON schemas
├── utils.py             # Utility functions (API keys, domain filtering)
├── prices.py            # Cost calculation classes per provider
└── py.typed             # Type hint support
```

### Scripts Structure (`scripts/`)
```
scripts/
├── {provider}/
│   ├── commands.sh      # Shell commands for querying and parsing
│   ├── query_*.py       # Query domains using provider APIs
│   └── parse_*.py       # Parse responses into structured data
└── processing/
    ├── gen_stats.py     # Generate statistical analysis
    ├── commands.sh      # Statistics generation commands
    └── update_frontend.sh # Update frontend data
```

### Key Components

#### API Clients (`api.py`)
- **BaseClient**: Abstract base class for all providers
- **Provider-specific clients**: OpenAI, Anthropic, Google, XAI, Together
- **Unified interface**: `query_model(domain, model)` method
- **Special handling**: Reasoning models (o1, o3, DeepSeek-R1) vs standard models
- **Error handling**: Graceful failure with None returns

#### Prompts (`prompts.py`)
- **SYS_BASE**: System prompt for credibility evaluation
- **USER_INSTRUCTION**: Domain rating instruction template
- **USER_FORMAT**: JSON format specification
- **DOMAIN_RATING_JSON_SCHEMA**: Strict JSON schema for validation
- **DomainRating**: Pydantic model for response validation

#### Cost Calculation (`prices.py`)
- **Provider-specific calculators**: Handle different token counting methods
- **Pricing data**: Up-to-date per-token costs for all models
- **Token types**: Input, output, cached, reasoning tokens
- **Cost breakdown**: Detailed token usage and cost calculation

#### Utilities (`utils.py`)
- **API key management**: Load keys from `api_keys.json`
- **Domain filtering**: Track processed vs pending domains
- **Resumable processing**: Skip already processed domains

## Data Pipeline

### 1. Domain Querying
```bash
# Pattern: query_<provider>.py <domain_list.csv> <provider> <model> <output_dir>
uv run query_openai.py ../../../data/source/dashboard_query_list.csv openai gpt-4o-mini output_dir
```

### 2. Response Parsing
```bash
# Pattern: parse_<provider>.py <provider> <model> <raw_responses_dir> <output.parquet>
uv run parse_openai.py openai gpt-4o-mini raw_responses/ parsed.parquet
```

### 3. Statistical Analysis
```bash
# Pattern: gen_stats.py <parquet_file> <model_name> <company> <reasoning_type>
uv run gen_stats.py parsed.parquet gpt-4o-mini OpenAI non_reasoning
```

### 4. Frontend Update
```bash
# Concatenate all JSON results for frontend
./scripts/processing/update_frontend.sh
```

## Command Patterns

### Query Commands
Each provider has standardized command patterns in `commands.sh`:
- Use `uv run` for all Python script execution
- Follow consistent argument order: `csv_file provider model output_dir`
- Output raw responses as individual `.txt` files per domain

### Parse Commands
- Input: Directory of raw response `.txt` files
- Output: Single `.parquet` file with structured data
- Include cost calculation and token counting
- Validate responses against JSON schema
- Filter invalid responses (rating outside 0-1 range)

### Statistics Commands
- Input: Parsed `.parquet` file
- Output: Statistical analysis JSON in `data/processed/`
- Calculate Spearman correlation with expert ratings
- Perform t-tests for political bias analysis
- Include significance testing and cost summaries

## API Key Management

Store API keys in `api_keys.json` at project root:
```json
{
  "openai": "your-openai-key",
  "anthropic": "your-anthropic-key",
  "google": "your-google-key",
  "xai": "your-xai-key",
  "together": "your-together-key"
}
```

## Development Notebooks

Located in `notebooks/` for exploratory analysis:
- `explore_*.ipynb`: Provider-specific testing and exploration
- `calculate_price.ipynb`: Cost analysis and pricing calculations
- `domain_alive.ipynb`: Domain availability checking

## Common Workflows

### Adding New Models
1. Update pricing in `prices.py`
2. Add model-specific handling in appropriate API client
3. Add commands to provider's `commands.sh`
4. Update cost calculator if token format differs

### Processing New Domains
1. Add domains to `data/source/dashboard_query_list.csv`
2. Run query commands for each provider
3. Parse responses to parquet format
4. Generate statistics
5. Update frontend data

### Debugging Failed Responses
- Check raw response files in `data/intermediate/raw_responses/`
- Examine parsing errors in console output
- Validate JSON schema compliance
- Check token usage and cost calculations

## Error Handling

- **API failures**: Graceful handling with None returns
- **JSON parsing**: `json-repair` library for malformed responses
- **Schema validation**: Pydantic for strict data validation
- **Resume capability**: Skip already processed domains
- **Cost tracking**: Detailed token usage monitoring