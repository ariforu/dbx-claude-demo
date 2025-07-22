"""
Payload classes for Databricks AI Gateway requests.
"""
class MessagePayload:
    def __init__(self, role, prompt, max_tokens):
        self.prompt = prompt
        self.max_tokens = max_tokens
        self.role = role

    def as_dict(self):
        return {
            "content": self.prompt,
            "max_tokens": self.max_tokens,
            "role": self.role
        }
