
import json

# def build_custom_prompt(model_name, user_query, temperature):
#     payload = {
#         "ai_engine": model_name,
#         "temp": temperature,
#         "prompt_text": user_query
#     } 
#     prompt = json.dumps(payload, indent = 4)
#     return prompt

# print("------ First Request --------")
# request_one = build_custom_prompt("claude-opus-3.6", "test one request with GPT and one with Claude", 0.3)
# print(request_one)

# print("------ Second Request --------")
# request_two = build_custom_prompt("gpt-4o", "using different temperatures", 0.7)
# print(request_two)





def calculate_token_cost(username, prompt_text):
    words = prompt_text.split()
    leng = len(words)
    cost = 0.002 * leng
    
    return print(f"User {username} sent a prompt with {leng} words. Estimated cost: ${cost}")

print( calculate_token_cost("Faheem", "What is the name of pakistan's capital?"))
print( calculate_token_cost("Hamza", "What is the real name of the institute?"))