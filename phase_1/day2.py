# import json

# # 1. The original Python Dictionary
# my_prompt = {
#     "role": "user",
#     "content": "Hello AI, what is the capital of France?",
#     "max_tokens": 100
# }

# # 2. Convert to JSON String (Simulating sending data to an API)
# # json.dumps() stands for "dump string"
# json_text = json.dumps(my_prompt, indent=4)

# print("--- Step 2: The JSON Text ---")
# print(type(json_text))
# print(json_text)
# print("\n") # Just adds a blank line for readability

# # 3. Convert back to Python Dictionary (Simulating receiving data from an API)
# # json.loads() stands for "load string"
# received_data = json.loads(json_text)

# print("--- Step 3: Converted Back to Dictionary ---")
# print(type(received_data))
# # Now we can extract specific pieces of information!
# print(f"The user said: {received_data['content']}")
# print("\n") # Just adds a blank line for readability

# # --- The Mini-Challenge ---

# # Pretend this is the raw text response that just came back from OpenAI over the internet
# fake_api_response = '{"id": "chatcmpl-123", "choices": [{"message": {"role": "assistant", "content": "The capital of France is Paris."}}]}'

# received_dataa = json.loads(fake_api_response)
# print(f"The AI said: {received_dataa['choices'][0]['message']['content']}")
# # TODO: Convert 'fake_api_response' into a Python dictionary named 'ai_data'
# # YOUR CODE HERE

# # TODO: Print ONLY the sentence: "The capital of France is Paris." by extracting it from 'ai_data'
# # YOUR CODE HERE



import json


ai_request = {
    "model" : "llama-3",
    "temperature" : 0.7,
    "message" : { "role" : "user", "content" : "Tell me a joke." }
}

ai_text = json.dumps(ai_request, indent=4)

print(ai_text)

incoming_response = {
    "status": "success",
    "usage": {
        "prompt_tokens": 12,
        "completion_tokens": 24
    },
    "candidates": [
        {
            "response_text": "Why did the developer go broke? Because he used up all his cache!"
        }
    ]
}

response_text = json.loads(json.dumps(incoming_response))  # Simulating receiving JSON response

print(response_text['candidates'][0]['response_text'])