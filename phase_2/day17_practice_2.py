import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY_2"))

phrases = [
    "Python asynchronous concurrency with asyncio",
    "Securing private enterprise data via local LLMs",
    "High-dimensional vector embedding coordinates"
]

response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=phrases
)

# Loop through the batch response embeddings
for i in range(len(phrases)):
    embedding_vector = response.embeddings[i].values

    print(f"\nBatch Item {i + 1}: '{phrases[i]}'")
    print(f"Total Dimensions: {len(embedding_vector)}")
    print(f"First 5 coordinates: {embedding_vector[:5]}")