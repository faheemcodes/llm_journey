import asyncio

async def main():
   print("Waiting for AI response...")
   await asyncio.sleep(2)
   print("Done waiting!")

asyncio.run(main())