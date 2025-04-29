# AI Model Local Deployment with LM Studio & LLM Website Hosted with Chat Terminal
This repository contains two distinct projects:

1. AI Model Local Deployment Using LM Studio: The backend setup for hosting and running a large language model (LLM) using LM Studio locally.

2. LLM Website Hosted with LLM Chat Terminal: A web-based front end that interacts with the locally hosted LLM backend through a chat interface, enabling users to ask questions and get responses based on the LLM's capabilities.

## AI Model Local Deployment Using LM Studio
This project sets up an LLM (Large Language Model) server using LM Studio. The model will be hosted locally to interact with other applications via HTTP API requests.
### Steps to Set Up LM Studio Server
**1. Install LM Studio:** Download and install LM Studio on your local machine. This tool allows you to run large language models locally.

* Visit the LM Studio documentation for installation details.

**2.Run the Model Server:** Start the LM Studio model server. By default, it will expose an API endpoint that accepts requests for completion, summarization, or any other tasks supported by the model.
**3.Update MODEL_API_URL:** In your Flask app or any other client application, make sure to point to the correct local server:
```bash
MODEL_API_URL = 'http://localhost:1234/v1/completions'
```
 **4.Run the Python Script**
 * For Web Hosted Run:
```bash
python app.py
```

* For Terminal chat Run:
```bash
test.py
```

## License
This project is licensed under the MIT License.
