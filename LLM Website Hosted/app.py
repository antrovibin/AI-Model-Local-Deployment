from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# API URL for the running model
MODEL_API_URL = 'http://192.168.27.106:1234/v1/completions'

# Function to send the prompt to the model and get the response
def get_model_response(prompt):
    payload = {
        "model": "gemma-2-2b-it",  # Ensure the model name is correct
        "prompt": prompt,
        "max_tokens": 100  # Adjust the number of tokens for the response
    }
    
    # Send request to the model
    response = requests.post(MODEL_API_URL, json=payload)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['text']
    else:
        return "Sorry, there was an error processing your request."

@app.route('/')
def home():
    """Render the main chat page."""
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    """Get the response from the model."""
    user_input = request.form['user_input']
    model_response = get_model_response(user_input)
    return jsonify({"response": model_response})

if __name__ == "__main__":
    app.run(debug=True)
