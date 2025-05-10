# LLM Domain Classification

A project to systematically probe multiple large language model (LLM) APIs with standardized prompts and analyze their responses.

## Objectives

- Systematically probe multiple LLM APIs (OpenAI, Anthropic, Google Gemini, TogetherAI) with standardized prompts
- Log and store responses in a structured, reproducible format for subsequent analysis
- Publish interactive results through a lightweight Vue 3 + Vite web application
- Keep backend (Python) and frontend (web) code cleanly separated

## Project Structure

```
project_root/
├── README.md
├── LICENSE
├── .gitignore
├── .env.sample                 # API keys (NOT committed)
├── data/                       # Raw + processed model outputs
│   ├── source/                   # Source files
│   ├── intermediate/             # Intermediate files
│   └── processed/                # Analyzed and formatted data
├── backend/                    # Python component
│   └── workflow/                 # The workflows
├── frontend/                   # Vue 3 + Vite app
└── .github/
    └── workflows/
        └── deploy-pages.yml    # build + push gh pages
```

## Setup

### Backend

1. Set up Python environment using `uv`:
   ```bash
   cd backend
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```

2. Configure environment variables:
   - Copy `.env.sample` to `.env`
   - Add your API keys and configuration

### Frontend

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start development server:
   ```bash
   npm run dev
   ```

## Development

### Backend Specifications
- Python environment managed with `uv`
- Local execution of Python tasks (no cloud/CI processing)
- Data storage formats:
  - Raw responses: JSON
  - Processed data: JSON and CSV

### Frontend Specifications
- Vue 3 + Vite web application
- Node.js version: 18+ LTS
- Styling: Tailwind CSS + DaisyUI
- Features:
  - Interactive visualization of backend results
  - Sub-pages for different research paper results
  - Responsive design for mobile and desktop

## Data Management

Each LLM response includes:
- Timestamp
- Model identifier
- Prompt used
- Complete response
- Metadata (temperature, tokens, etc.)

Processed results include aggregated statistics and analysis.

## Deployment

- Frontend: Automatic deployment to GitHub Pages via GitHub Actions
- Backend: Local processing with results committed to data directory
- Environment: Managed via `.env` files (not committed to repository)

## License

See [LICENSE](LICENSE) file for details.
