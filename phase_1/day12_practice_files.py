import asyncio
# practice Task 2
async def load_document(file_name, load_time):
    print(f"Loading file into memory: {file_name}...")
    await asyncio.sleep(load_time)
    print(f"Successfully loaded: {file_name}")

async def main():
    await asyncio.gather(
        load_document("company_policies.pdf", 2.0),
        load_document("software_architecture.md", 0.5),
        load_document("api_documentation.json", 1.2)
    )
    
asyncio.run(main())