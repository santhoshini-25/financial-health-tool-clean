# Financial Health Assessment Tool

A comprehensive platform for small and medium enterprises (SMEs) to assess financial health using AI, data visualizations, and secure processing.

## Features

- **Data Upload**: Support for CSV, XLSX, and PDF files for revenue, expenses, and other financial metrics.
- **AI Insights**: Powered by Hugging Face AI (with mock fallback) for creditworthiness scores, risk analysis, optimization suggestions, and product recommendations.
- **Visualizations**: Interactive bar charts using Chart.js to display financial metrics like revenue, expenses, and profit.
- **Multilingual Support**: English and Hindi translations using react-i18next.
- **Security**: Data encryption, CORS-enabled, and secure API handling.
- **Integrations**: Mock banking (Plaid) and GST APIs for future expansion.
- **Reports**: PDF generation capability for investor-ready reports.

## Tech Stack

- **Frontend**: React.js, Chart.js, Axios, react-i18next
- **Backend**: FastAPI, Python, Pandas, SQLAlchemy
- **Database**: PostgreSQL
- **AI**: Hugging Face Inference API (free tier)
- **Deployment**: Local (for demo); can be deployed to Render/Vercel

## Problem Solved

SMEs often lack tools for financial analysis, leading to poor decisions. This tool provides affordable, AI-driven insights, visualizations, and multilingual support to help businesses optimize finances, identify risks, and access suitable products without expensive consultants.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git
- PostgreSQL (optional for DB)

### Backend Setup
1. Navigate to `backend/` folder.
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Set environment variables in `.env` (see `.env.example`)
6. Run: `uvicorn main:app --reload`
7. API docs at `http://127.0.0.1:8000/docs`

### Frontend Setup
1. Navigate to `frontend/` folder.
2. Install dependencies: `npm install`
3. Run: `npm start`
4. App at `http://localhost:3000`

### Usage
- Upload a financial file (e.g., CSV with Revenue/Expenses).
- View AI insights and interactive chart.
- Switch languages for accessibility.

## Demo Video
[Insert YouTube/Google Drive link here after uploading]

## Contributing
Feel free to fork and contribute. Ensure tests pass before PR.

## License
MIT License
