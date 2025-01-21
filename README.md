# Agentic AI Projects

This repository contains code and documentation for three exciting projects I worked on recently, showcasing the potential of Agentic AI systems in various domains.

## Projects Overview

### 1. Financial AI Agent with Phidata
- **Description**: A financial agent capable of analyzing stocks, fetching news, and providing recommendations.
- **Technologies Used**: Phidata, YFinance, DugDugGo.
- **Features**:
  - Stock analysis using YFinance.
  - Web search integration with DugDugGo.
  - Multi-agent workflow combining financial data and web insights.
- **How to Run**:
  1. Set up the environment using `requirements.txt`.
  2. Configure API keys in `.env` file.
  3. Run `financial_agent.py`.

### 2. Multi-Agentic AI with Vector Databases
- **Description**: A multi-agent system leveraging vector databases for semantic search and efficient data retrieval.
- **Technologies Used**: Vector Databases, Phidata.
- **Features**:
  - Combines multiple agents for handling complex workflows.
  - Efficient data retrieval using vector embeddings.
- **How to Run**:
  1. Install dependencies from `requirements.txt`.
  2. Configure database connection settings.
  3. Run `multi_agent.py`.

### 3. Video Summarization Agent with Google Gemini
- **Description**: A video summarization application that analyzes video content, answers contextual questions, and performs supplementary web searches.
- **Technologies Used**: Google Gemini AI, Streamlit, AWS S3 (for cloud integration).
- **Features**:
  - Upload videos for analysis (up to 200MB locally or larger via S3).
  - Summarize videos and extract key insights.
  - Perform web searches related to video content.
- **How to Run**:
  1. Install dependencies from `requirements.txt`.
  2. Set up Google API key in `.env` file.
  3. Run `app.py` using Streamlit: `streamlit run app.py`.

## Prerequisites
- Python >=3.8
- API keys for relevant services (e.g., Google Gemini, Phidata).
- Cloud setup (optional) for large file handling.

## Installation
1. Clone the repository:
2. Install dependencies:
3. Set up environment variables in `.env` file.

## Future Work
- Expand multi-agent capabilities with additional tools and APIs.
- Enhance scalability with more robust cloud integrations.
- Explore new use cases in domains like healthcare, education, and e-commerce.

## Contributions
Feel free to fork this repository and contribute enhancements or new features! Open an issue or submit a pull request if you have suggestions.

---

Happy coding! 🚀
