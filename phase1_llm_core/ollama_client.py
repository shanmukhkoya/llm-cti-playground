import requests

import os

def query_ollama(prompt, model=None):
    """
    Query the Ollama API.

    Args:
        prompt (str): The prompt to send.
        model (str, optional): The model to use. If not provided, uses the OLLAMA_DEFAULT_MODEL environment variable or 'tinyllama'.

    Returns:
        str: The response from the API.
    """
    if model is None:
        model = os.getenv("OLLAMA_DEFAULT_MODEL", "tinyllama")
    """
    Sends a prompt to the Ollama API and returns the generated response.

    Args:
        prompt (str): The input prompt to send to the model.
        model (str, optional): The name of the model to use. Defaults to "tinyllama".

    Returns:
        str: The generated response from the model.

    Raises:
        requests.HTTPError: If the HTTP request returned an unsuccessful status code.
    """
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json().get("response", "")
