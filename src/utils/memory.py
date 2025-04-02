
class Memory:
    """Handles conversation history for the chatbot."""

    def __init__(self, max_history=50):
        self.messages = []
        self.max_history = max_history

    def add_message(self, role, content):
        """Add a new message to the history and matain history size."""
        self.messages.append({"role": role, "content" : content})
        if len(self.messages) > self.max_history:
            self.messages.pop(0)

    def get_history(self):
        """Retrive the conversation history."""
        return self.messages