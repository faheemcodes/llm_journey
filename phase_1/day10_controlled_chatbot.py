import os
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

generation_config = {
    "temperature": 0.0
}

model = genai.GenerativeModel(
    model_name= "gemini-3.6-flash",
    generation_config= generation_config,
    system_instruction= "You are a dull software engineer who hates code."
)

response = model.generate_content("do you hate coding")

print(response.text)

# chat = model.start_chat(history=[])


# print("\n=== SARCASTIC CODE REVIEWER CHATBOT ===")
# while True:
#     prompt = input("\nAsk Anything (or type 'exit' to quit): ")
    
#     if prompt.lower() == 'exit':
#         print("Exiting Chatbot. Goodbye!")
#         break
    
#     response = chat.send_message(prompt)
#     print("\nAI Response:")
#     print(response.text)

