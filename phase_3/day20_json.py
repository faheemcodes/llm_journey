import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY_2"))

# 1. Define the exact structure you want using Pydantic
class SupportTicketAnalysis(BaseModel):
    ticket_id: int = Field(description="The ID number of the support ticket.")
    customer_name: str = Field(description="Name of the customer.")
    issue_category: str = Field(description="Category like Billing, Technical, or Account.")
    urgency_level: str = Field(description="Low, Medium, or High.")
    action_required: str = Field(description="Brief summary of what needs to be done.")

# 2. Provide raw, unstructured text
email_text = """
Hi Support, my name is Sarah Jenkins. My account ID is 4492. 
I am completely locked out of my dashboard and my billing renewal is tomorrow! 
I need someone to reset my credentials immediately. This is super urgent.
"""

# 3. Call the model and enforce the response schema
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"Analyze this customer support email and extract the details: {email_text}",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=SupportTicketAnalysis
    ),
)

print(response.text)
print("\nData Type of response.text:", type(response.text))