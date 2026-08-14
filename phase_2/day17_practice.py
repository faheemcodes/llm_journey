import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

client= genai.Client(api_key= os.getenv("GOOGLE_API_KEY_2"))

phrases = [
    "Our company policy requires two-factor authentication for all cloud services.",
    "Employees must use 2FA to log into corporate servers."
]

response = client.models.embed_content(
    model= "gemini-embedding-001",
    contents= phrases
)

for res in range(len(phrases)):
    embedding_vector = response.embeddings[res].values

    print(f"\n Original Text: '{phrases[res]}'")
    print(f"Total Dimensions in Vector Array: {len(embedding_vector)}")
    print(f"First 5 numbers of the embedding vector: {embedding_vector[:5]}")