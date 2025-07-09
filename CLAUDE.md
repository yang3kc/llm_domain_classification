# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a research project that evaluates how well Large Language Models (LLMs) can assess the credibility and categorize news sources. The project includes a Python backend for querying multiple LLM providers and a Vue.js frontend dashboard for displaying results.

## Development Setup

### Backend Setup
```bash
cd backend
uv sync
uv add --editable ./llmdomainrating/
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev          # Development server
npm run build        # Production build
npm run format       # Code formatting
```

## Key Commands

### Data Processing
- Generate statistics from parsed responses: `uv run gen_stats.py <parquet_file> <model_name> <company> <reasoning_type>`
- Update frontend data: `./scripts/processing/update_frontend.sh`

### Model Querying
Each provider has its own scripts in `backend/scripts/`:
- OpenAI: `./scripts/openai/commands.sh`
- Anthropic: `./scripts/anthropic/commands.sh`
- Google: `./scripts/google/commands.sh`
- Together: `./scripts/together/commands.sh`
- XAI: `./scripts/xai/commands.sh`

### Parquet Data Inspection
Use `parquet-tools` to inspect data files:
```bash
parquet-tools show -n 10 <path_to_parquet_file>    # View first 10 rows
parquet-tools inspect <path_to_parquet_file>        # View schema
```

## Architecture

### Backend Structure
- `backend/llmdomainrating/`: Core Python package with API clients for different LLM providers
- `backend/scripts/`: Provider-specific scripts for querying models and processing responses
- `backend/notebooks/`: Jupyter notebooks for exploratory analysis

### Core Components
- `api.py`: Unified API clients for OpenAI, Anthropic, Google, Together, and XAI
- `prompts.py`: Standardized prompts and JSON schemas for domain credibility rating
- `utils.py`: Utility functions for data processing
- `prices.py`: Cost calculation utilities

### Data Flow
1. Raw responses stored in `data/intermediate/raw_responses/`
2. Parsed responses stored in `data/intermediate/parsed_responses/` as parquet files
3. Statistical analysis generates JSON files in `data/processed/`
4. Frontend reads from `frontend/public/data/results.json`

### Frontend Structure
- Vue 3 + Vite application with Tailwind CSS and DaisyUI
- Router-based navigation between Home, About, and Paper Rating views
- FontAwesome icons for company logos
- Responsive design with statistical visualizations

## API Keys
Store API keys in `api_keys.json` (not committed to git). The structure should match the provider names used in the codebase.

## Testing
No specific test framework configured. Verify functionality by running the processing scripts and checking output files.

## Data Files
- Source data: `data/source/dashboard_query_list.csv`
- Intermediate parquet files contain parsed LLM responses
- Final results aggregated in `data/processed/` as JSON files per model