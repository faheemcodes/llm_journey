import asyncio

async def broadcast_prompt(model_id, prompt_text, response_delay):
    print(f"[{model_id}] Processing prompt: '{prompt_text}'...")
    await asyncio.sleep(response_delay)
    print(f"[100% Complete] {model_id} answered: 'Processed successfully!'")
    
async def main():
    results = await asyncio.gather(
        broadcast_prompt("Model-Alpha", "Analyze database logs", 1.5),
        broadcast_prompt("Model-Beta", "Analyze database logs", 0.8),
        broadcast_prompt("Model-Gamma", "Analyze database logs", 2.2)
    )
    
    print("\n--- All Model Responses Received ---")
    
    for ans in results:
        print(ans)
    
asyncio.run(main())  
    