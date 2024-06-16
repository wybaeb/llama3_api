import os
from flask import Flask, request, jsonify
from llama_cpp import Llama
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API token from environment variables
API_TOKEN = os.getenv('API_TOKEN', 'your_secure_token')

# Initialize the LLaMA model
SYSTEM_PROMPT = "Ты — Сайга, русскоязычный автоматический ассистент. Ты разговариваешь с людьми и помогаешь им."
MODEL_PATH = "model-q4_K.gguf"
N_CTX = 8192
TOP_K = 30
TOP_P = 0.9
TEMPERATURE = 0.6
REPEAT_PENALTY = 1.1

model = Llama(
    model_path=MODEL_PATH,
    n_ctx=N_CTX,
    n_parts=1,
    verbose=True,
)

app = Flask(__name__)

@app.route('/interact', methods=['POST'])
def interact():
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header.split(" ")[1] != API_TOKEN:
        return jsonify({"error": "Forbidden"}), 403

    data = request.json
    user_message = data.get('text', '')

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.append({"role": "user", "content": user_message})
    
    response_text = ""
    for part in model.create_chat_completion(
        messages,
        temperature=TEMPERATURE,
        top_k=TOP_K,
        top_p=TOP_P,
        repeat_penalty=REPEAT_PENALTY,
        stream=True,
    ):
        delta = part["choices"][0]["delta"]
        if "content" in delta:
            response_text += delta["content"]

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
