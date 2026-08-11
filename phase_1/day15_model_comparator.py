import os 
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai
import time

load_dotenv()
genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

async def compare_models(model_name, prompt_text):
    model = genai.GenerativeModel(model_name)
    start_time = time.time()
    response = await asyncio.to_thread( model.generate_content, prompt_text)
    duration = time.time() - start_time
    return f"[{model_name}] executed the Query: '{response.text}'... in {duration}"

async def main():
    results = await asyncio.gather(
       compare_models("gemini-3.5-flash-lite", "Explain microservices vs monolith architecture in 2 sentences."),
       compare_models("gemini-3.6-flash", "Explain microservices vs monolith architecture in 2 sentences.") 
    )
    
    print("\n Different Model reselts------------")
    
    for ans in results:
        print(ans)

asyncio.run(main())