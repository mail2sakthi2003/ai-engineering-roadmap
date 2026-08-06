from pathlib import Path
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

# Load the .env file that sits right next to this script.
# We use __file__ instead of relying on the current directory, because
# on Windows especially, "where you ran python from" and "where the
# script lives" are often two different folders — this way it always works.
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# ChatAnthropic automatically looks for ANTHROPIC_API_KEY in the environment —
# we don't have to pass it in manually.
llm = ChatAnthropic(model="claude-sonnet-4-6", max_tokens=100)

# invoke() sends one message and waits for the full response (no streaming yet)
response = llm.invoke("Say hello in one sentence.")

print("Response text:", response.content)
print("Tokens used:", response.usage_metadata)