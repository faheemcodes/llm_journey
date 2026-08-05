import json

# This looks like valid JSON, but let's see what happens
bad_json_string = '{"model": "gpt-4o", "temperature": 0.5' # Missing closing curly brace!

try:
    # Attempt to parse the broken string
    parsed_data = json.loads(bad_json_string)
    print("Success! Parsed data:", parsed_data)

except json.JSONDecodeError:
    # If JSON parsing fails, catch it here instead of crashing
    print("ERROR: Failed to parse AI response. The JSON structure is corrupted.")

print("Program continues running safely without crashing!")

