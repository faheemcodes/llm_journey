import os
from dotenv import load_dotenv
from google import genai
import numpy as np

## COSINE SIMILARITY - CHALLENGE

load_dotenv()
client = genai.Client(api_key= os.getenv("GOOGLE_API_KEY_2"))


article_0 = "How to reset your corporate Wi-Fi password on Windows and Mac."
article_1 = "Steps to submit a reimbursement claim for travel expenses."
article_2 = "Troubleshooting VPN connection errors when working remotely."
article_3 = "Guidelines for ordering new hardware peripherals like keyboards and monitors."
query= "My VPN keeps dropping connection, how do I fix it?"

response = client.models.embed_content(
    model= "gemini-embedding-001",
    contents= [article_0, article_1, article_2, article_3, query]
)

ans_0 = np.array(response.embeddings[0].values)
ans_1 = np.array(response.embeddings[1].values)
ans_2 = np.array(response.embeddings[2].values)
ans_3 = np.array(response.embeddings[3].values)
que = np.array(response.embeddings[4].values)

def cosine_similarity(a, b):
    return np.dot(a, b) / ((np.linalg.norm(a)) * (np.linalg.norm(b)))

ans_0 = cosine_similarity(ans_0, que)
ans_1 = cosine_similarity(ans_1, que)
ans_2 = cosine_similarity(ans_2, que)
ans_3 = cosine_similarity(ans_3, que)

print(f"Similarity check between article 1 and query: {ans_0:.4f}")
print(f"Similarity check between article 2 and query: {ans_1:.4f}")
print(f"Similarity check between article 3 and query: {ans_2:.4f}")
print(f"Similarity check between article 4 and query: {ans_3:.4f}")