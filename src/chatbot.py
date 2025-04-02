from llm_client import LLMClient
from utils.memory import Memory

class Chatbot:
    """Main chatbot class that interacts with users."""

    def __init__(self, provider="openai"):
        self.llm_client = LLMClient(provider)
        self.memory=Memory()

    def chat(self, user_input):
        """Handles user input, maintains history, and fetches LLM response."""
        self.memory.add_message("user", user_input)
        messages = self.memory.get_history()
        ai_response = self.llm_client.get_response(messages)
        self.memory.add_message("system", ai_response)
        return ai_response