import asyncio


# Task 1

# async def stream_token(token_word, delay):
#     print(f"Streaming: {token_word}...")
#     await asyncio.sleep(delay)
#     print(f"Delivered: {token_word}")

# async def main():
#     await stream_token("Hello", 3.0)
#     await stream_token("LLM", 2.0)
#     await stream_token("Engineer", 1.0)

# asyncio.run(main())

#Task 2

async def call_ai_with_timeout(prompt, delay):
    print(f"Sending prompt: '{prompt}' to cloud... ")
    try:
        await asyncio.wait_for(asyncio.sleep(delay), timeout=2.0)
        print("Response received successfully!")
    except asyncio.TimeoutError as e:
        print("Warning: AI API request timed out! Retrying...", e)

async def main():
    await call_ai_with_timeout("Fast prompt", 1.0)
    await call_ai_with_timeout("Slow prompt", 3.0)

asyncio.run(main())
    
    
        
    
    
    