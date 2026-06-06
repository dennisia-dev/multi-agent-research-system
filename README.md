# Multi-Agent LLM Research System

An autonomous multi-agent AI system that performs end-to-end research using planning, web search, memory, and self-critique loops powered by a local LLM (Phi-2).

---

## Overview

This project implements a modular **AI research agent system** that simulates how an intelligent assistant would conduct research:

- Breaks down complex queries into structured tasks (Planner Agent)
- Retrieves real-time information from the web (Search Tool)
- Stores and organizes evidence (Memory Module)
- Generates structured research reports (Writer via LLM)
- Critically evaluates and improves outputs (Critic Agent)

The system follows a multi-step reasoning pipeline similar to modern agent frameworks.

---

## System Architecture
User Query
→
Planner Agent (Task Decomposition)
→
Search Tool (DuckDuckGo Web Search)
→
Memory Module (Evidence Storage)
→
Writer Agent (Report Generation using Phi-2)
→
Critic Agent (Self-Evaluation)
→
Refinement Loop
→
Final Answer

---

## ⚙️ Features

- Multi-agent architecture (Planner, Researcher, Writer, Critic)
- Tool-augmented reasoning using live web search
- Structured task planning (JSON-based planning)
- Persistent memory for evidence accumulation
- Self-critique and refinement loop for better outputs
- Fully local inference using Microsoft Phi-2
- Modular and extensible Python codebase

---

## 🛠️ Tech Stack

- Python
- PyTorch
- HuggingFace Transformers
- Microsoft Phi-2
- DuckDuckGo Search API
- Streamlit (optional UI support)

---

## 📁 Project Structure
llm-research-agent/
│

├── agents/

│ ├── planner.py

│ ├── research_agent.py

│ ├── critic.py

│

├── tools/

│ ├── search_tool.py

│

├── memory/

│ ├── memory.py

│

├── models/

│ ├── model_loader.py

│

├── main.py

├── requirements.txt

└── README.md

---

## ▶️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/dennisia-dev/llm-research-agent
cd llm-research-agent

2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

🚀 How to Run
Run the CLI agent
python main.py
```

## 💡 Example Usage
Input:
What are the effects of AI on software engineering jobs?

Output:
Structured research plan
Web-sourced evidence
Generated research report
Critic feedback
Improved final answer

## 🧠 Key Concepts Implemented

1. Multi-Agent Architecture

The system decomposes reasoning into specialized agents:

Planner → task breakdown
Search tool → external knowledge retrieval
Writer → report generation
Critic → evaluation and feedback

2. Tool-Augmented LLM

The model is enhanced with external web search capability to access real-time information.

3. Memory System

Stores intermediate evidence across tasks to maintain context throughout reasoning.

4. Self-Critique Loop

The system evaluates its own output and refines it using structured feedback.

## 📌 Why This Project Matters

This project demonstrates:

LLM agent system design
Prompt engineering for structured reasoning
Tool integration with language models
Multi-step autonomous workflows
Self-improving AI systems

It is comparable in design philosophy to modern agent frameworks.

## 🚀 Future Improvements

1. Add Streamlit UI dashboard for interactive use

2. Integrate FAISS or ChromaDB for semantic memory

3. Parallelize tool execution for faster research

4. Add support for multiple LLMs (Mistral, LLaMA)

5. Deploy as a web app (Render / HuggingFace Spaces)

6. Add LangGraph-style orchestration

## 👨‍💻 Author

Built as a multi-agent AI systems project demonstrating autonomous reasoning, tool use, and self-improving LLM workflows.

## ⭐ If you like this project

If this project helped or inspired you, consider giving it a ⭐ on GitHub.

---

If you want next, I can help you:
- make this **look like a top 1% GitHub repo (badges, banner, diagram)**
- write your **resume bullets**
- write your **LinkedIn post that gets recruiter attention**
- or add **Streamlit UI in 10 minutes**

Just tell me 👍
