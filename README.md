# 📄 Docling RAG Agent

*A lightweight Retrieval-Augmented Generation (RAG) system powered by
Gemini, ChromaDB, Docling & Pydantic-AI.*

## 🚀 Overview

Docling RAG Agent is a command-line RAG application capable of
processing **PDF, DOCX, PPTX, Markdown**, and other text-based document
formats.\
It uses:

-   **Docling** → to convert + chunk documents\
-   **Gemini Embeddings** → to embed chunks\
-   **ChromaDB** → to store & retrieve embeddings\
-   **Pydantic-AI** → to structure the RAG agent\
-   **Google Gemini** → as the LLM backend

With just two commands, you can **ingest documents** and then **query
your knowledge base** through an interactive CLI.

## ✨ Features

-   🔥 Supports multiple document types --- PDF, DOCX, PPTX, MD\
-   🧩 Hybrid chunking using Docling's **HybridChunker**\
-   🧠 Semantic search powered by **Gemini embeddings**\
-   🗂️ Persistent vector store using **ChromaDB**\
-   🤖 RAG agent built using **Pydantic-AI + Gemini**\
-   🧵 Clean project structure, simple CLI interface

## 📁 Project Structure

    .
    ├── embedding.py
    ├── ingestion.py
    ├── rag_agent.py
    ├── model.py
    ├── tools/
    │   └── search_knowledge_base.py
    ├── sample_data/
    │   ├── alfez_mansuri_resume.pdf
    │   ├── Basic_presentation.pptx
    │   ├── tweeter_post_generator.md
    │   └── Welcome_to_Word.docx
    ├── requirements.txt
    ├── .env.example
    └── chroma_db/       # Created automatically (ignored in git)

## ⚙️ Installation

### 1️⃣ Clone the repo & create a virtual environment

``` bash
git clone https://github.com/AMalfez/docling_rag_agent.git
cd docling_rag_agent

python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scriptsctivate        # Windows
```

### 2️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

### 3️⃣ Setup Environment Variables

Copy `.env.example` → `.env`\
Update:

``` env
GOOGLE_GENAI_API_KEY="your_api_key_here"
CHROMA_GOOGLE_GENAI_API_KEY="your_api_key_here"
```

## 📥 Ingesting Documents (Build the Vector DB)

``` bash
python ingestion.py
```

## 🔍 Run the RAG Agent (Ask Questions)

``` bash
python rag_agent.py
```

## 🧠 How Knowledge Search Works

The file `tools/search_knowledge_base.py` exposes:

``` python
search_knowledge_base(query, db_name="test_db", n_results=3)
```

## 🛠️ Future Improvements

-   Streaming responses\
-   UI dashboard\
-   Incremental ingestion\
-   Better prompt orchestration

## 🤝 Contributing

PRs and suggestions welcome!

## ⭐ Support

If you found this helpful, please ⭐ the repository!
