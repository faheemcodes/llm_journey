# Phase 1 & Week 2: Complete Day-by-Day LLM Engineering Study Notes

## Day 1: Virtual Environments & Local Setup
* **What it does:** Isolates project dependencies using Python's built-in `venv` module so that package versions don't conflict globally across your machine.
* **Key Command:** `python -m venv myenv` followed by activating it via `myenv\Scripts\activate`.
* **Pro Tip:** If Windows blocks your activation script, you override it by running PowerShell as Administrator and using `Set-ExecutionPolicy Unrestricted`.

## Day 2: Data Types & JSON Serialization
* **What it does:** Translates live Python dictionaries into plain text strings (`json.dumps()`) to transmit over the internet to APIs, and converts incoming text back into Python objects (`json.loads()`).
* **Why it matters:** LLM servers (like OpenAI or Google) do not understand Python dictionaries in memory; they require universal string formats like JSON.

## Day 3: Control Flow & Loops
* **What it does:** Uses `for` loops, `while` loops, and `if/elif/else` chains with the modulo operator (`%`) to filter data or process tokens.
* **Crucial Rule:** Always place your strictest/most specific condition at the top of an `if/elif` chain so it doesn't get bypassed prematurely.

## Day 4: Functions & Modularity
* **What it does:** Encapsulates logic into reusable blocks that accept parameters. 
* **Best Practice:** Use the `return` keyword instead of trapping output inside a terminal `print()` statement so other parts of your program can reuse the data.

## Day 5: Error Handling (`try/except/finally`)
* **What it does:** Anticipates runtime failures (like empty user inputs or disk permission locks), manually raises errors (`raise ValueError`), catches them gracefully with `except`, and executes cleanup routines via `finally`.

## Day 6: Object-Oriented Programming (Classes & Objects)
* **What it does:** Combines data (attributes via `self`) and actions (methods) inside a reusable architectural blueprint (`class`), then instantiates functional objects from it.

## Day 7: Week 1 Mini-Project (CLI Task & Prompt Logger)
* **What it does:** Ties together classes, lists, dictionaries, file handling (`open('file.txt', 'w')`), JSON dumps, and a `while True` interactive menu loop to build a fully functional command-line application.

## Day 8: Environment Variables (`os` & `.env`)
* **What it does:** Keeps secret API keys out of your code and public repositories by storing them in a hidden `.env` file and loading them dynamically into Python via `python-dotenv` and `os.getenv()`.

## Day 9: Live AI API Requests & Stateful Chat Memory
* **What it does:** Connects programmatically to cloud LLM providers, manages model string identifiers, and uses `model.start_chat(history=[])` alongside `chat.send_message(prompt)` to maintain active, multi-turn conversational memory.

## Day 10: System Instructions & Generation Config (Temperature)
* **What it does:** Shapes model behavior and persona using `system_instruction`, and controls response creativity and determinism using `generation_config={"temperature": 0.2}`.

## Day 11: Asynchronous Programming & Timeouts (`asyncio`)
* **What it does:** Uses `async def`, `await`, and `asyncio.sleep()` to perform non-blocking pauses. Protects applications from hanging cloud APIs using `asyncio.wait_for()` with strict deadline control.

## Day 12: Concurrent Task Gathering (`asyncio.gather`)
* **What it does:** Fires off multiple asynchronous tasks simultaneously so they run as a pack and finish based on their individual speeds rather than waiting sequentially.

## Day 13 & 14: Real API Concurrency & Thread Offloading (`asyncio.to_thread`)
* **What it does:** Fixes performance bottlenecks when calling synchronous third-party SDKs inside an async event loop by offloading heavy execution to background worker threads, preventing local UI/CPU freezes.

## Day 15: Multi-Model AI Comparator Project
* **What it does:** Combines concurrency, threads, execution timers, and result gathering into a real-world evaluation dashboard that benchmarks multiple models side-by-side.
