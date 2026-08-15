import os
from dotenv import load_dotenv
from google import genai
import numpy as np

## COSINE SIMILARITY

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY_2"))

# Two sentences with similar meanings but different words
sentence_1 = "Our company policy requires two-factor authentication for all cloud services."
sentence_2 = "Employees must use 2FA to log into corporate servers."
sentence_3 = "What is the best recipe for chocolate chip cookies?"

response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=[sentence_1, sentence_2, sentence_3]
)

v1 = np.array(response.embeddings[0].values)
v2 = np.array(response.embeddings[1].values)
v3 = np.array(response.embeddings[2].values)

# Function to calculate ##Cosine Similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / ((np.linalg.norm(a) * np.linalg.norm(b)))

sim_1_2 = cosine_similarity(v1, v2)
sim_1_3 = cosine_similarity(v1, v3)

print(f"Similarity between Security Sentence 1 and Security Sentence 2: {sim_1_2:.4f}")
print(f"Similarity between Security Sentence 1 and Cookie Recipe Sentence 3: {sim_1_3:.4f}")