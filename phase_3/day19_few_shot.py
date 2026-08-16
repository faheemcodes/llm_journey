import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY_2"))

# Few-shot prompt with examples of turning technical jargon into ELI5 (Explain Like I'm 5)
prompt = """
Convert technical terms into simple, fun explanations for a 5-year-old.

Example 1:
Technical: API
Simple: A magical waiter that takes your order to the kitchen and brings the food back.

Example 2:
Technical: Cloud Computing
Simple: Storing your toys in a giant toy box at a friend's house instead of your own room so you can play with them anywhere.

Example 3:
Technical: Database
Simple: 
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",  # or gemini-2.5-flash / gemini-1.5-flash depending on your setup
    contents=prompt
)

print(response.text)