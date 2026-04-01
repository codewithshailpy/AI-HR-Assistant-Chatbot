# AI HR Assistant Chatbot

An AI-powered HR assistant chatbot designed to help employees and visitors quickly get answers to HR-related queries using company knowledge base documents.

The chatbot uses **Retrieval Augmented Generation (RAG)** with a vector database to provide accurate responses based on internal HR documents.

The system is designed to be **scalable, reliable, and easily integrated** with company websites, employee portals, or other applications.

---

# Project Goals

* Reduce HR workload by automating repetitive employee queries
* Provide instant access to HR policies and company information
* Enable employees to create HR support tickets when needed
* Build a scalable AI system that can integrate with multiple platforms

---

# Key Features

## AI HR Assistant

Employees can ask questions such as:

* What is the leave policy?
* What is the notice period?
* How do I apply for maternity leave?

The chatbot retrieves answers from company HR documents.

---

## Embeddable Chat Widget

The chatbot can be embedded into:

* Company website
* Employee portal
* Internal applications


---

## HR Ticket Creation

If the chatbot cannot answer a query, users can create an HR support ticket.

Ticket information stored:

* Employee / visitor name
* Email
* Query description
* Ticket status
* Creation timestamp

---

## Knowledge Base from Documents

The chatbot learns from:

* HR policy documents
* Employee handbook
* Leave policies
* IT support guides
* FAQ documents

These documents are converted into embeddings and stored in a vector database.

---

# Technology Stack

| Layer               | Technology                    |
| ------------------- | ----------------------------- |
| Frontend Widget     | JavaScript Chat Widget        |
| Backend API         | Python (FastAPI)              |
| Vector Database     | ChromaDB                      |
| LLM                 | OpenAI API                    |
| Document Processing | LangChain/Python              |
| Deployment          | AWS                           |

---

# System Architecture

```
Employees / Visitors
        |
        v
Chat Widget (Website / Portal)
        |
        v
Backend API (FastAPI)
        |
        v
Vector Database (ChromaDB)
        |
        v
OpenAI API
        |
        v
Generated Response
```

---

# Repository Structure

```
AI-HR-Assistant-Chatbot
│
├── backend
│   ├── app
│   │   ├── api
│   │   │   ├── chat.py
│   │   │   └── ticket.py
│   │   │
│   │   ├── services
│   │   │   ├── rag_service.py
│   │   │   ├── embedding_service.py
│   │   │   └── llm_service.py
│   │   │         
│   │   │
│   │   ├── models
│   │   │   └── schemas.py
│   │   │
│   │   └── main.py
│
├── ingestion
│   ├── document_loader.py
│   ├── chunking.py
│   └── embed_documents.py
│
|
|
|── chroma_db.py
|
|
├── data/
│   ├── raw_docs/hr/        
│   └── processed/
|
|
├── widget
│   ├── widget.js
│   ├── widget.css
│   └── index.html
│
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository_url>
cd AI-HR-Assistant-Chatbot
```

---

## 2. Create Python Environment

```bash
python -m venv venv
```

Activate environment:

Linux / Mac

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
CHROMA_DB_DIR=./chroma_db
MODEL_NAME=gpt-4o-mini
```

---

# Document Ingestion

Place HR documents inside:

```
data/hr_docs/
```

Example documents:

* leave_policy.pdf
* employee_handbook.pdf
* benefits_policy.pdf

Run ingestion pipeline:

```bash
python ingestion/embed_documents.py
```

This will:

1. Load documents
2. Chunk text
3. Generate embeddings
4. Store vectors in ChromaDB

---

# Running the Backend

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

API will run at:

```
http://localhost:8000
```

---

# Chat API Example

Endpoint:

```
POST /chat
```

Request:

```json
{
 "question": "What is the notice period?"
}
```

Response:

```json
{
 "answer": "The notice period is 60 days according to HR policy."
}
```

---

# HR Ticket API

Endpoint:

```
POST /ticket
```

Example request:

```json
{
 "name": "John Doe",
 "email": "john@company.com",
 "query": "My leave balance is incorrect"
}
```
---


# Expected Business Impact

* Reduce HR workload
* Faster employee support
* Centralized knowledge access
* Improved employee experience

---
# Note
This project uses sample HR policy documents for demonstration purposes only.


# License

Internal project for personal use.
