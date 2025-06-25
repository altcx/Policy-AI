# 🧭 AI Policy Navigator - Project Roadmap & Tech Stack

## 📌 Project Overview

Build an AI-powered tool that allows users to query local government policies and legal documents using natural language. The system uses LLMs + Retrieval-Augmented Generation (RAG) to answer user questions by extracting context from scraped PDFs (including messy scans).

**Primary goal:** Prototype a working version that can run locally or with minimal cloud usage, suitable for showcasing on a resume, GitHub, and portfolio.

---

## 🔧 Tech Stack Overview

### 📂 Document Ingestion

| Component   | Tool/Library                 | Purpose                        |
| ----------- | ---------------------------- | ------------------------------ |
| PDF Parsing | `PyMuPDF`, `pdfplumber`      | Extract clean text from PDFs   |
| OCR         | `Tesseract`                  | Extract text from scanned PDFs |
| Chunking    | Custom Python or `LangChain` | Split documents for embedding  |

### 🧠 Embeddings + Vector Store

| Component  | Tool/Library                                                | Notes                                 |
| ---------- | ----------------------------------------------------------- | ------------------------------------- |
| Embeddings | `bge-small-en`, `MiniLM`, `text-embedding-3-small (OpenAI)` | Chosen for quality vs speed trade-off |
| Vector DB  | `FAISS`, `Chroma`                                           | Store and retrieve document chunks    |

### 🤖 Language Models (LLMs)

| Type      | Model                 | Platform           | Notes                              |
| --------- | --------------------- | ------------------ | ---------------------------------- |
| Local LLM | **Mistral 7B**        | Ollama             | Best local model for reasoning     |
| Local LLM | **Phi-3 Mini (1.8B)** | Ollama / llama.cpp | Low-resource fallback              |
| Cloud LLM | **GPT-4o**            | OpenAI API         | High quality, limited by cost      |
| Cloud LLM | **GPT-3.5-turbo**     | OpenAI API         | Cheaper, good enough in many cases |

---

## 🧩 Architecture Summary

```text
User Query → Embed → Search Vector DB → Top-k Contexts → Prompt LLM → Response
```

### 🏗️ Components:

1. **Ingestion Pipeline**

   - Parse PDFs
   - OCR if needed
   - Chunk into manageable segments
   - Store embeddings in Vector DB

2. **Query Engine**

   - Embed incoming question
   - Perform vector similarity search
   - Construct a prompt with top-k chunks
   - Run prompt through LLM
   - Return answer

3. **Interface (Optional UI)**

   - Terminal-based Q&A tool OR
   - Lightweight web UI using Streamlit or Flask

---

## 💻 Development Plan

### Phase 1: Setup & Local PDF Parsing

-

### Phase 2: RAG Core

-

### Phase 3: LLM Integration

-

### Phase 4: Interface & Demo

-

---

## 🔐 Cost & Hosting Strategy

- No full-scale hosting planned
- Primary focus on local inference + small API usage for demos
- Store models and vectors locally
- Include optional `.env` config for OpenAI API key

---

## 📁 Suggested Directory Structure

```bash
ai-policy-navigator/
├── data/              # Raw and processed PDFs
├── ocr/               # OCR tools and scripts
├── chunks/            # Preprocessed document text
├── index/             # FAISS/Chroma vector storage
├── app/               # Core RAG logic
│   ├── retrieval.py
│   ├── query_engine.py
│   └── main.py
├── frontend/          # (Optional) Streamlit or Flask app
├── notebooks/         # Experiments and prototypes
├── requirements.txt
└── README.md
```

---

## 📝 Resume/GitHub Tips

- Include a **short write-up** of your architecture and technical choices
- Create a **screencast or walkthrough demo**
- Document sample queries and expected outputs
- Use GitHub Issues or a Project Board to track progress

