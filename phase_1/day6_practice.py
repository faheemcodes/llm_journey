class PromptManager:
    def __init__(self, system_prompt, max_tokens):
        self. system_prompt = system_prompt
        self.max_tokens = max_tokens
    
    def format_payload(self, user_input):
        my_dict = {
            "system": self.system_prompt,
            "tokens": self.max_tokens,
            "user": user_input
        }
        return my_dict

first_prompt = PromptManager("You are a helpful coding assistant.", 500)

print(first_prompt.format_payload("Faheem"))