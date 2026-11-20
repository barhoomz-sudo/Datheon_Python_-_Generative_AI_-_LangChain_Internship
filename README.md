# AI-Powered Invoice Extraction Pipeline

A Python application that uses Google's Gemini API to extract structured information from unstructured invoice text and convert it into validated JSON data.

## Overview

This project demonstrates how Large Language Models (LLMs) can be integrated into Python applications to automate document information extraction.

It uses Gemini to interpret invoice text, Pydantic to validate the extracted information, and Python to organize the extraction pipeline.

## Features

- Extract invoice information from unstructured text.
- Generate structured JSON responses using Gemini.
- Validate extracted data using Pydantic models.
- Verify that invoice totals match the sum of individual item prices.
- Handle empty input and invalid responses.
- Automated tests using pytest and mocking.

## Technologies Used

- Python 3
- Google Gemini API
- Google GenAI Python SDK
- Pydantic
- pytest
- python-dotenv
- unittest.mock

## Project Structure

```text
├── data/
│   ├── invoices/
│   └── resumes/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── extractor.py
│   ├── prompts.py
│   └── schemas.py
├── tests/
│   ├── __init__.py
│   ├── test_extractor.py
│   └── test_schemas.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_DIRECTORY
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GEMINI_API=your_gemini_api_key
```

Never commit your actual API key to GitHub.

## Usage

Place your invoice text in the input file configured in `src/main.py`.

Run the application:

```bash
python -m src.main
```

The application sends the invoice text to Gemini, receives structured JSON data, and validates the result using Pydantic.

## Running Tests

Execute the test suite:

```bash
pytest -v
```

The tests cover:

- Invoice schema validation.
- Invalid invoice totals.
- Missing and invalid fields.
- Empty invoice input.
- Successful extraction.
- Invalid Gemini responses.

## Learning Objectives

This project explores:

- Integrating LLM APIs with Python.
- Prompt engineering.
- Structured output generation.
- Data validation with Pydantic.
- Separation of application responsibilities.
- Unit testing and mocking external dependencies.

## Author
My LinkedIn profile - https://www.linkedin.com/in/ibrahim-hussain-237699433/
Developed as part of the Datheon Generative AI & LangChain Internship.