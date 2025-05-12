# Backend

This directory contains the backend code for the dashboard.

## Structure

```
backend/
├── llmdomainrating/          # Local python package to fetch and process data
├── notebook/                 # Temporary notebooks for development
└── scripts/                  # Python scripts
```

## Setup

1. Set up Python environment using `uv`:
   ```bash
   cd backend
   uv sync
   ```

## Local development

We have built a `llmdomainrating` package to facilitate the local development.
The package is not published to PyPI, so you need to install it locally.
This can be done by running the following command:

```bash
uv add --editable ./llmdomainrating/
```