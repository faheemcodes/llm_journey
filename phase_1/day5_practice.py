#Task 1

def safe_api_call(user_input):
    try:
        length = len(user_input)
        if length == 0:
            raise ValueError("Prompt cannot be empty!")
        else:
            message =f"AI Processing complete for: {user_input}"
            return message
    except ValueError as e:
        return e
    finally: print("--- Request finished ---")


print(safe_api_call("Hello, AI!"))
print(safe_api_call(""))


#Task 2

class TokenLimitExceededError(Exception): pass

def process_tokens(token_count):
    try:
        if token_count > 1000:
            raise TokenLimitExceededError("Error: Request dropped. Token count exceeds maximum context window!")
        else:
            message = f"Success: Processed {token_count} tokens safely."
            return message
    except TokenLimitExceededError as e:
        return e
    

print(process_tokens(450))
print(process_tokens(1500))
        