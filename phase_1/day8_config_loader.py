import os 
from dotenv import load_dotenv

load_dotenv()

my_dict ={
    "model_name": os.getenv("AI_MODEL_NAME"),
    "temperature": float(os.getenv("AI_TEMPERATURE")),
    "max_token_limit": int(os.getenv("MAX_TOKEN_LIMIT"))
}

print(my_dict)
print("Model Name type:", type(my_dict["model_name"]))
print("Temperature type:", type(my_dict["temperature"]))
print("Max Tokens type:", type(my_dict["max_token_limit"]))



