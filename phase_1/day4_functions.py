import json

# 1. Defining the function
def create_ai_payload(user_message, token_limit):
    # This dictionary represents our standardized API payload structure
    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "user", "content": user_message}
        ],
        "max_tokens": token_limit
    }
    
    # Convert the dictionary into a JSON string and return it
    json_string = json.dumps(payload, indent=4)
    return json_string

# 2. Calling the function multiple times with different inputs
print("--- Request 1 ---")
request_one = create_ai_payload("Explain quantum computing in one sentence.", 50)
print(request_one)

print("\n--- Request 2 ---")
request_two = create_ai_payload("Write a Python script to reverse a string.", 150)
print(request_two)