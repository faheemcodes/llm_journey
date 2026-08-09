import os 
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-3.6-flash")

chat = model.start_chat(history=[])

print("\n=== GEMINI CONTINUOUS CHATBOT ===")
while True:
    prompt = input("\nAsk Anything (or type 'exit' to quit): ")
    
    if prompt.lower() == 'exit':
        print("Exiting Chatbot. Goodbye!")
        break
    
   
    response = chat.send_message(prompt)
    print("\nAI Response:")
    print(response.text)

