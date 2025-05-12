# LLM Domain Classification project

![logo](logo.png)

## Overview

As LLMs increasingly help curate and filter information in search engines, chatbots, and recommendation systems, their ability to accurately evaluate news sources directly impacts the quality and reliability of information they provide to users.
This project evaluates how well Large Language Models (LLMs) can assess the credibility and categorize news sources.

See our [dashboard](https://yang3kc.github.io/llm_domain_classification/) for the results and methods.

## Citation

If you find this project useful, please cite it as follows:

```bibtex
@misc{yang2024accuracypoliticalbiasnews,
      title={Accuracy and Political Bias of News Source Credibility Ratings by Large Language Models},
      author={Kai-Cheng Yang and Filippo Menczer},
      year={2024},
      eprint={2304.00228},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2304.00228},
}
```

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
   uv sync
   ```


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
