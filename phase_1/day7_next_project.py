import json 

class PromptCostCalculator:
    def __init__(self, model_name, rate_per_token):
        self.model_name = model_name
        self.rate_per_token = rate_per_token
    
    def estimate_cost(self, prompt_text):
        self.prompt_text = prompt_text
        words = len(self.prompt_text.split())
        rate = words * self.rate_per_token
        return rate
    
    def generate_payload(self, user_prompt):
        cost = self.estimate_cost(user_prompt)
        
        try:
            if not isinstance(self.prompt_text, str) and len(self.prompt_text.split()) == 0:
                raise ValueError("Prompt cannot be empty or invalid!")
            else:
                payload = {
                    "model": self.model_name,
                    "prompt": user_prompt,
                    "estimated_cost": cost
                }
                return payload
            
        except ValueError as e:
            return {"error": str(e)}


ai_calculator = PromptCostCalculator("gpt-4o", 0.00002)


while True:
    print("\n=== AI PROMPT COST & PAYLOAD MANAGER ===")
    print("1. Calculate Prompt Cost & Generate Payload")
    print("2. Exit")
    
    choice = input("Enter your choice (1-2): ")
    
    if choice == "1":
        # Get user prompt input
        user_prompt = input("Enter your AI prompt: ")
        
        # Generate the payload (which includes our error handling safety net!)
        result = ai_calculator.generate_payload(user_prompt)
        
        print("\n--- Result ---")
        print(result)
        
    elif choice == "2":
        print("Exiting Manager. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please enter 1 or 2.")

