import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

class OllamaClient:
    """Handles requests to the LLM API."""

    def __init__(self):
        self.base_url = os.getenv("OLLAMA_BASE_URL")
        self.api_key = os.getenv("OLLAMA_API_KEY")
        self.model = os.getenv("OLLAMA_MODEL")

    def get_response(self, messages: list):
        """Fetch response from ollama."""
        openai = OpenAI(base_url=self.base_url, api_key=self.api_key)
        stream = openai.chat.completions.create(
            model=self.model,
            messages = messages,
            stream=True
        )        
        return stream
        