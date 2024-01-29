# Gemini LLM Application

Gemini LLM (Language Model) Application is a Streamlit-based project that leverages Google's Generative AI for natural language processing and image understanding. This project allows users to interact with Gemini Pro and Gemini models to generate responses based on user inputs or questions.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [License](#license)

## Introduction

Gemini LLM Application provides a simple user interface for interacting with Google's Generative AI models, specifically Gemini Pro and Gemini. The application is built using Streamlit and utilizes the power of natural language understanding and image processing.

## Getting Started

To run the Gemini LLM Application locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/5PCD3/Gemini-LLM-Application.git
    cd <repository-directory>
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Create a virtual environment (optional but recommended):**
    ```bash
    conda create -p venv python==3.10 -y
    conda activate venv/  
    ```

4. **Set up your environment variables:**
    - Create a `.env` file in the project root and add your Google API key:
        ```env
        GOOGLE_API_KEY="your-google-api-key"
        ```

5. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

6. **Access the application in your browser at http://localhost:8501.**

## Usage

The application provides two main functionalities:

### Gemini Pro Vision

1. Upload an image using the file uploader.
2. Enter an input prompt.
3. Click the "Tell me about the image" button to generate a response based on the image and input prompt.

### Q&A Demo

1. Enter a question in the input field.
2. Click the "Ask The Question" button to generate a response based on the provided question.

## Dependencies

- [Streamlit](https://streamlit.io/)
- Google Generative AI
- python-dotenv

## Configuration

Ensure you have set up your Google API key in the `.env` file:

```env
GOOGLE_API_KEY="your-google-api-key"


