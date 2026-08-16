import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY_2"))

# Prompt explicitly asking for step-by-step reasoning
prompt = """
A support technician starts their shift with 15 unresolved tickets. 
During the first hour, they resolve 4 tickets, but 3 new tickets come in. 
In the second hour, they resolve double the number of tickets they resolved in the first hour, and 5 new tickets come in. 
How many unresolved tickets do they have at the end of the second hour?

Let's think step-by-step to arrive at the correct answer.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(response.text)