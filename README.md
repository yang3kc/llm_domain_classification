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

# Technical Details

## Project Structure

```
project_root/
├── README.md
├── LICENSE
├── .gitignore
├── .env                          # API keys (NOT committed)
├── data/                         # Raw + processed model outputs
│   ├── source/                   # Source files
│   ├── intermediate/             # Intermediate files
│   └── processed/                # Analyzed and formatted data
├── backend/                      # Backend code
├── frontend/                     # Vue 3 + Vite app for the dashboard
└── .github/
    └── workflows/
        └── deploy-pages.yml     # build + push gh pages
```

## Backend

See [backend](backend) for details.

## Frontend

See [frontend](frontend) for details.

## Contributing

You are welcome to contribute to the project by opening an issue or a pull request.
Questions and requests can be sent to [Kai-Cheng Yang](mailto:yang3kc@gmail.com).