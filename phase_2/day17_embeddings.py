import os
from dotenv import load_dotenv
from google import genai

## EMBEDDINGS

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY_2"))

text_to_embed = "Securing private enterprise data with local LLMs."

# Call the modern embedding endpoint
response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=text_to_embed,
)

# Extract the embedding values from the modern response structure
embedding_vector = response.embeddings[0].values

print(f"Original Text: '{text_to_embed}'")
print(f"Total Dimensions in Vector Array: {len(embedding_vector)}")
print(f"First 5 numbers of the embedding vector: {embedding_vector[:5]}")
