# LLM Domain Classification

A project to systematically probe multiple large language model (LLM) APIs with standardized prompts and analyze their responses.

## Features

- Probe multiple LLM APIs (OpenAI, Anthropic, Google Gemini, TogetherAI)
- Structured data collection and analysis
- Interactive visualization through Vue 3 web application
- Automated deployment to GitHub Pages

## Project Structure

```
project_root/
├── data/                       # Raw + processed model outputs
│   ├── raw/                   # Original LLM responses
│   └── processed/             # Analyzed and formatted data
├── backend/                    # Python component
│   ├── requirements.txt       # Python dependencies
│   ├── src/                   # Source code
│   └── tests/                 # Test files
├── frontend/                   # Vue 3 + Vite app
│   ├── package.json          # Node.js dependencies
│   ├── src/                  # Source code
│   └── tests/                # Test files
```

## Setup

### Backend

1. Set up Python environment:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
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

- Backend: Python 3.11+
- Frontend: Node.js 18+ LTS
- Testing:
  - Backend: pytest
  - Frontend: Vitest + Cypress

## Deployment

The frontend automatically deploys to GitHub Pages on push to main branch.

## License

See [LICENSE](LICENSE) file for details.
