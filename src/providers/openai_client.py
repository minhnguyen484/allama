import os
import openai
from dotenv import load_dotenv

load_dotenv(override=True)

class OpenAIClient:
    """Handles request to OpenAI API."""

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.model = os.getenv("OPENAI_MODEL", "gpt-4")

    def get_response(self, messages: list):
        """Fetch response form OpenAI."""
        stream = openai.chat.completions.create(
            model = self.model,
            messages = messages,
            stream=True
        )
        result = ""
        for chunk in stream:
            result = chunk.choices[0].delta.content or ""
            yield result