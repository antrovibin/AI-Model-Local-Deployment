import requests

# The API URL of your running model
MODEL_API_URL = 'http://193:1234/v1/completions' #Your Model Url

def get_user_input():
    """Get prompt from user via terminal input"""
    prompt = input("Please enter the prompt (or type 'exit' to quit): ")
    return prompt

def get_model_response(prompt):
    """Send the prompt to the model and get the response"""
    payload = {
        "model": "gemma-2-2b-it",  # Ensure the model name is correct
        "prompt": prompt,
        "max_tokens": 100  # You can adjust the number of tokens for the response
    }
    
    # Send the request to the API
    response = requests.post(MODEL_API_URL, json=payload)
    
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to get response from the model."}

def display_response(response):
    """Display the model's response"""
    if "choices" in response:
        text = response['choices'][0]['text']
        print("Model Response:\n", text)
    else:
        print(response.get("error", "Unknown error"))

def main():
    """Main function to run the process"""
    while True:
        prompt = get_user_input()  # Get the prompt from the user
        
        # Exit the loop if the user types 'exit'
        if prompt.lower() == 'exit':
            print("Exiting the program.")
            break
        
        response = get_model_response(prompt)  # Get the model's response
        display_response(response)  # Display the response to the user

if __name__ == "__main__":
    main()
