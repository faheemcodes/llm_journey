import os 
from dotenv import load_dotenv

load_dotenv(".env")
key = os.getenv("AI_MODEL_NAME")
print(key)