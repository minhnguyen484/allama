from providers.ollama_client import OllamaClient
from providers.openai_client import OpenAIClient

class LLMClient:
    """Factory class to select the approriate LLM provider."""

    def __init__(self, provider="openai"):
        self.provider = provider.lower()
        self.client = self._get_client()

    def _get_client(self):
        """Returns the approriate LLM client based on provider."""
        if self.provider == "openai":
            return OpenAIClient()
        elif self.provider == "ollama":
            return OllamaClient()
        else:
            raise ValueError("Unsupported LLM provider")

    def get_response(self, messages):
        """Gets response from the selected LLM."""
        return self.client.get_response(messages)