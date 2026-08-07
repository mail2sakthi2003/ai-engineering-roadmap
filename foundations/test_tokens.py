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

    ##OUTPUT##

# Prompt (2 chars): input_tokens=8
# Prompt (18 chars): input_tokens=12
# Prompt (118 chars): input_tokens=33 

# Concept 1: Tokens

# What they actually are: an LLM doesn't read words — it reads tokens, which are chunks of 
# text (often sub-word pieces). Roughly: 1 token ≈ 4 characters ≈ ¾ of an English word. "Terraform" 
# might be one token; "OIDC" might be split into two or three.

# Why it matters: you're billed per token (input + output), and every model has a maximum number of'
# ' tokens it can process in one go — this is the context window. Tokens are the actual unit of cost '
# 'and capacity in everything you'll build.

# Run it and look at how character count vs. token count scales — this builds your intuition for
# "roughly how many tokens is this document going to cost me," which matters a lot once 
# you're chunking documents for RAG next week.