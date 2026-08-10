import asyncio

async def fetch_model(model_name, delay):
    print(f"Query started in {model_name}...")
    await asyncio.sleep(delay)
    print(f"Query Successfully fininshed of {model_name}.")

async def main():
    await asyncio.gather(
        fetch_model("Gemini-Fast", 1.0), 
        fetch_model("Claude-Pro", 3.0), 
        fetch_model("GPT-Mini", 2.0)
        )

asyncio.run(main())