import os 
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

async def async_query_gemini(prompt_text):
    model = genai.GenerativeModel("gemini-3.6-flash")
    response = await asyncio.to_thread(model.generate_content, prompt_text)
    return response.text

async def main():
    result = await asyncio.gather(
        async_query_gemini("What is an LLM in one sentence?"),
        async_query_gemini("What is Python in one sentence?")
    )
    
    print("\n--- All Model Responses Received ---")
    
    for ans in result:
        print(f"\n{ans}")
        
asyncio.run(main())