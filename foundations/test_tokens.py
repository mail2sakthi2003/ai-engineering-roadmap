# foundations/test_tokens.py
from pathlib import Path
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv(dotenv_path=Path(__file__).parent / ".env")
llm = ChatAnthropic(model="claude-sonnet-4-6", max_tokens=50)

prompts = [
    "Hi",
    "What is Terraform?",
    "Explain in detail how OIDC federated authentication works for CI/CD pipelines, including the trust relationship setup.",
]

for p in prompts:
    response = llm.invoke(p)
    usage = response.usage_metadata
    print(f"Prompt ({len(p)} chars): input_tokens={usage['input_tokens']}")