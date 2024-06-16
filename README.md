# Simple API with LLM

This project provides a simple API using a large language model (LLM) to interact with users. The API is built using Flask and integrates the LLaMA model for natural language processing.

## Project Overview

This API serves as a backend for a chatbot that interacts with users in Russian. It uses the LLaMA model, which is a powerful language model for generating human-like text. The chatbot can respond to various queries and assist users with their needs.

## Technical Requirements

- Python 3.9 or later
- Flask
- llama_cpp
- dotenv

## Model Download

The model file `model-q4_K.gguf` needs to be downloaded from Hugging Face. Follow these instructions to download the model:

1. Visit the [model page on Hugging Face](https://huggingface.co/IlyaGusev/saiga_llama3_8b_gguf).
2. Download the `model-q4_K.gguf` file.
3. Place the downloaded model file in the same directory as the `app.py` file.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/wybaeb/mos_hack1.git
    cd mos_hack1
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the project directory and add the following line:
    ```
    API_TOKEN=your_secure_token
    ```

5. Run the Flask app:
    ```bash
    python app.py
    ```

## API Usage

To interact with the API, send a POST request to the `/interact` endpoint with the user's message. The `Authorization` header must contain the API token.

Example request:
```bash
curl -X POST http://localhost:5000/interact \
    -H "Authorization: Bearer your_secure_token" \
    -H "Content-Type: application/json" \
    -d '{"text": "Как погодка сегодня?"}'
