# AI Engineering Roadmap

A hands-on learning repo documenting my path from Senior Cloud Engineer toward
Principal AI Engineer — built project by project, all running locally first.
Cloud deployment of any of these is a deliberate backlog item, not an oversight.

See [`AI_Learning_Roadmap.md`](./AI_Learning_Roadmap.md) for the full plan this
repo follows, and [`notes_nl.md`](./foundations/notes_nl.md) for a plain-English
walkthrough of the ML concepts used in `foundations/test_ml.py`.

---

## Structure

This repo is organized into two parent tracks, plus a shared foundations module:

```
ai-engineering-roadmap/
├── foundations/          # Week 1 — shared setup and core concepts
├── rag-bot/               # Track A, Project 1 — RAG over personal docs
├── devops-agent/          # Track A, Project 2 — cloud/DevOps tool-calling agent
├── langgraph-triage/       # Track A, Project 3 — multi-agent incident triage
├── adk-agent/              # Track A, Project 4 — custom agent on Google ADK
└── (ml projects added as Track B progresses)
```

---

## Foundations (Week 1)

Shared prerequisite for both tracks below — environment setup and core concepts
(tokens, context windows, embeddings, local vector search, ML train/test split).

| Script | What it demonstrates |
|---|---|
| `foundations/test_llm.py` | First LLM call via the Anthropic API through LangChain |
| `foundations/test_tokens.py` | How prompt length relates to token usage/cost |
| `foundations/test_embeddings.py` | Turning text into vectors and comparing meaning via cosine similarity |
| `foundations/test_chroma.py` | A real local vector database — add, persist, and semantically query documents |
| `foundations/test_ml.py` | A classic ML train/test pipeline (see `notes_nl.md` for the plain-English explanation) |

---

## Track A — Generative AI

RAG, agents, and orchestration — the higher-leverage skill set for AI Engineer roles right now.

| Project | Core Skill | Status |
|---|---|---|
| **A1 — Personal Knowledge RAG Bot** | RAG, embeddings, vector DB | Upcoming |
| **A2 — Cloud/DevOps Tool-Calling Agent** | LangChain agents, tool calling | Upcoming |
| **A3 — Multi-Agent Incident Triage** | LangGraph, stateful orchestration | Upcoming |
| **A4 — Custom Agent with Google ADK** | ADK, MCP integration | Upcoming |

**A1 — Personal Knowledge RAG Bot:** a CLI/Streamlit app that answers questions
over my own documents (Terraform module docs, runbooks) with citations back to
source — the full RAG pipeline: ingest, chunk, embed, retrieve, generate.

**A2 — Cloud/DevOps Tool-Calling Agent:** an agent that reasons about cloud
questions and calls real local tools (parsing Terraform plans, reading local
AWS cost output) — read-only, local, no live cloud mutations.

**A3 — Multi-Agent Incident Triage:** a LangGraph workflow — alert comes in,
retrieve relevant runbook (reusing A1's vector store), classify severity, draft
remediation, pause for human approval. Demonstrates conditional routing,
checkpointing, and human-in-the-loop steps.

**A4 — Custom Agent with Google ADK:** extends existing MCP/ADK exploration —
porting agent logic into Google's ADK framework, integrated with MCP.

---

## Track B — Machine Learning

Classic supervised/unsupervised ML, all built on cloud/cost data — the
differentiator that shows "real ML," not just LLM prompting.

| Project | Core Skill | Status |
|---|---|---|
| **B1 — Cloud Cost Anomaly Detector** | Regression / anomaly detection | Upcoming |
| **B2 — Incident Severity Classifier** | Classification | Upcoming |
| **B3 — Cloud Usage Forecasting** | Time-series forecasting | Upcoming |
| **B4 — Workload Clustering for Cost Optimization** | Unsupervised / clustering | Upcoming |

---

## Setup

```bash
git clone https://github.com/mail2sakthi2003/ai-engineering-roadmap.git
cd ai-engineering-roadmap

python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
# source venv/bin/activate     # Mac/Linux

pip install langchain langchain-anthropic langgraph chromadb \
            scikit-learn pandas matplotlib jupyter python-dotenv sentence-transformers
```

Create a `.env` file inside `foundations/` with your Anthropic API key:
```
ANTHROPIC_API_KEY=your-key-here
```

## Running the foundations scripts

```bash
python foundations/test_llm.py
python foundations/test_tokens.py
python foundations/test_embeddings.py
python foundations/test_chroma.py
python foundations/test_ml.py
```

---

## Roadmap

Full plan, sequencing options, and the reasoning behind each project:
[`AI_Learning_Roadmap.md`](./AI_Learning_Roadmap.md)

For the plain-English explanation of the ML train/test concept in
`test_ml.py`: [`foundations/notes_nl.md`](./foundations/notes_nl.md)
