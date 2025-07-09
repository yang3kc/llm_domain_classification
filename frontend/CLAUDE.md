# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with the frontend code in this repository.

## Overview

Vue 3 + Vite dashboard application for displaying LLM domain credibility evaluation results. Uses Tailwind CSS with DaisyUI for styling and displays statistical analysis of model performance.

## Development Setup

```bash
npm install          # Install dependencies
npm run dev          # Start development server (opens at http://localhost:5173)
npm run build        # Build for production
npm run preview      # Preview production build
npm run format       # Format code with Prettier
```

## Tech Stack

- **Vue 3**: Composition API with `<script setup>`
- **Vite**: Build tool with hot reload
- **Tailwind CSS 4**: Utility-first CSS framework
- **DaisyUI**: Tailwind component library with "pastel" theme
- **Vue Router**: Client-side routing
- **FontAwesome**: Icon library
- **Prettier**: Code formatting

## Architecture

### File Structure
```
src/
├── App.vue              # Root component with router view
├── main.js              # App entry point with FontAwesome setup
├── assets/
│   ├── main.css         # Tailwind configuration
│   └── *.svg            # Company logos (OpenAI, Anthropic, Google, etc.)
├── components/
│   ├── NavBar.vue       # Sticky navigation with router links
│   ├── ModelResults.vue # Main dashboard with data tables
│   └── Footer.vue       # Footer component
├── composables/
│   └── useCompanyLogos.js # Logo management utilities
├── views/
│   ├── HomeView.vue     # Dashboard page
│   ├── AboutView.vue    # About page
│   └── PaperRatingView.vue # Paper information page
└── router/
    └── index.js         # Route definitions
```

### Key Components

#### ModelResults.vue
- **Purpose**: Main dashboard component displaying accuracy and bias tables
- **Data source**: Fetches from `public/data/results.json` (newline-delimited JSON)
- **Key features**:
  - Company filtering with logo display
  - Reasoning model filtering
  - Sortable correlation and bias results
  - Tooltips explaining metrics
  - Responsive tables with hover effects

#### useCompanyLogos.js
- **Purpose**: Composable for managing company logos
- **Functions**:
  - `formatCompany()`: Returns HTML with logo and company name
  - `getCompanyLogo()`: Returns logo URL for a company
  - `companyLogos`: Object mapping company names to SVG imports

### Styling System
- **Tailwind CSS 4**: Uses new CSS Layer syntax
- **DaisyUI**: Provides semantic component classes
- **Theme**: "pastel" theme with custom container styles
- **Responsive**: Mobile-first approach with responsive tables

### Data Flow
1. Frontend fetches from `public/data/results.json`
2. Data is newline-delimited JSON format
3. Each line contains model statistics (correlation, bias, costs)
4. Tables are dynamically filtered and sorted
5. Company logos are dynamically loaded from assets

### Configuration
- **Vite config**: Production base path set to `/llm_domain_classification/`
- **Path aliases**: `@/` maps to `src/`
- **Dev server**: Auto-opens browser on port 5173

## Data Format

The `results.json` file expects newline-delimited JSON with these fields:
- `model_name`: Model identifier
- `company`: Company name (must match logo assets)
- `n`: Number of domains rated
- `rho`: Spearman correlation coefficient
- `rho_p`: P-value for correlation
- `t`: T-statistic for bias
- `t_p`: P-value for bias
- `reasoning_type`: "reasoning" or "non_reasoning"
- `left_n`, `right_n`: Domain counts by political leaning
- `date`: ISO date string
- `cost`: Total cost in USD

## Development Notes

- Components use Vue 3 Composition API exclusively
- All styling uses Tailwind utility classes
- Company logos are SVG imports, not runtime assets
- Tables use DaisyUI table classes for consistent styling
- Tooltips provide detailed metric explanations
- New models (within 30 days) get "New" badges
- Statistical significance shown with star notation