import os 
from dotenv import load_dotenv
import google.generativeai as genai

## EMBEDDINGS

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY_2"))

model = genai.GenerativeModel("gemini-3.6-flash")

prompt= "Hello LLM Engineer, welcome to Phase 2!"
response = model.count_tokens(prompt)

print(f"The prompt is: '{prompt}'")
print(f"Total tokens used: {response.total_tokens}")