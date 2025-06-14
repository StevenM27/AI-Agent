import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

# Get the API key from our environment variable
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Check the command line arguments for the prompt
if len(sys.argv) < 2:
    print("Usage: main.py \"Prompt for AI\"")
    sys.exit()

user_prompt = sys.argv[1]
verbose = False

# Check for verbose flag
if len(sys.argv) >= 3 and sys.argv[2] == "--verbose":
    verbose = True

# List of messages to keep track of the conversation 
# between the user and the AI.
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]


# Create a client and pass in the provided prompt
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages
)

if verbose:
    print(f"\nUser prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")

print(response.text)
