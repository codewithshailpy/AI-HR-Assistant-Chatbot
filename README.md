# AI HR Assistant Chatbot

An AI-powered HR assistant chatbot designed to help employees and visitors quickly access HR-related information using an intelligent, document-driven system.

The solution leverages **Retrieval-Augmented Generation (RAG)** with a vector database to provide accurate, context-aware answers from internal HR documents.

It is built to be **scalable, modular, and embeddable** across websites, employee portals, and internal tools.

---

# 🚀 Project Objectives

* Automate repetitive HR queries
* Provide instant, 24/7 employee support
* Centralize HR knowledge access
* Reduce operational load on HR teams
* Enable seamless escalation via ticketing system

---

# ✨ Key Features

## 🧠 AI HR Assistant

Employees can ask questions such as:

* What is the leave policy?
* What is the notice period?
* How can I apply for maternity leave?

The chatbot retrieves relevant information from internal documents and generates contextual responses.

---

## 💬 Embeddable Chat Widget

A lightweight, plug-and-play JavaScript widget that can be embedded into:

* Company websites
* Employee portals
* Internal dashboards

### Integration Example

```html
<script src="http://<your-server>/chat.js"></script>
```

✔ No frontend dependency
✔ Works across platforms
✔ Easy to customize

---

## 🎫 HR Ticket Creation

If a query cannot be resolved:

* Users can raise support tickets
* HR team gets notified
* Ticket lifecycle can be tracked

### Ticket Data Includes

* Name
* Email
* Query
* Status
* Timestamp

---

## 📚 Knowledge Base from Documents

Supports ingestion of:

* HR policy documents
* Employee handbook
* Leave policies
* IT guidelines
* FAQs

Documents are processed, chunked, embedded, and stored in a vector database for semantic search.

---

# 🧱 Technology Stack

| Layer               | Technology                       |
| ------------------- | -------------------------------- |
| Frontend Widget     | JavaScript (Embeddable Widget)   |
| Backend API         | Python (FastAPI)                 |
| Vector Database     | ChromaDB                         |
| Embeddings          | HuggingFace / OpenAI             |
| LLM                 | HuggingFace (Local) / OpenAI API |
| Document Processing | Python / LangChain               |
| Deployment          | AWS (planned)                    |

---

# 🏗️ System Architecture

```
User (Employee / Visitor)
        ↓
Chat Widget (Website / Portal)
        ↓
Backend API (FastAPI)
        ↓
Vector Database (ChromaDB)
        ↓
RAG Pipeline
        ↓
LLM (HuggingFace / OpenAI)
        ↓
Response
```

---

# 📂 Repository Structure

```
AI-HR-Assistant-Chatbot
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── chat.py
│   │   │   └── ticket.py
│   │   │
│   │   ├── services/
│   │   │   ├── rag_service.py
│   │   │   ├── embedding_service.py
│   │   │   └── llm_service.py
│   │   │
│   │   ├── models/
│   │   │   └── schemas.py
│   │   │
│   │   └── main.py
│
├── ingestion/
│   ├── document_loader.py
│   ├── chunking.py
│   └── embed_documents.py
│
├── data/
│   ├── raw_docs/hr/
│   └── processed/
│
├── chroma_db/              # Vector database (generated)
│
├── widget/                 # Embeddable chatbot widget
│   ├── chat.js
│   ├── style.css
│   └── index.html
│
└── README.md
```

---

# ⚙️ Setup Instructions

## 1. Clone Repository

```bash
git clone <repository_url>
cd AI-HR-Assistant-Chatbot
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env` file:

```
OPENAI_API_KEY=your_api_key   # Optional (if using OpenAI)
CHROMA_DB_DIR=./chroma_db
MODEL_NAME=gpt-4o-mini
```

---

# 📥 Document Ingestion

Place HR documents inside:

```
data/raw_docs/hr/
```

Run ingestion:

```bash
python ingestion/embed_documents.py
```

### This process:

* Loads documents
* Splits into chunks
* Generates embeddings
* Stores vectors in ChromaDB

---

# ▶️ Running the Backend

```bash
uvicorn app.main:app --reload
```

API available at:

```
http://localhost:8000
```

---

# 🔗 API Endpoints

## Chat Endpoint

```
POST /chat
```

### Request

```json
{
  "question": "What is the leave policy?"
}
```

### Response

```json
{
  "answer": "Employees are entitled to 20 paid leaves annually..."
}
```

---

## Ticket Endpoint

```
POST /ticket
```

---

# 🌐 Widget Integration

## Local Testing

```bash
cd widget
python -m http.server 5500
```

Open:

```
http://localhost:5500
```

---

## Embed in Any Website

```html
<script src="http://localhost:5500/chat.js"></script>
```

---

## ⚠️ Enable CORS in Backend

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

# ⚡ Current Capabilities

✔ RAG-based chatbot
✔ Vector search using ChromaDB
✔ Embeddable chat widget
✔ Local (free) and OpenAI-based modes
✔ REST API architecture

---

# 🚧 Upcoming Enhancements

* Authentication (employee login)
* Chat history persistence
* Streaming responses (real-time typing)
* Ticket System
* Admin dashboard for HR
* Analytics & usage tracking

---

# 📈 Business Impact

* Reduced HR workload
* Faster employee query resolution
* Improved employee experience
* Centralized knowledge access

---

# ⚠️ Note

This project uses sample HR documents for demonstration purposes only.

---

# 📄 License

Internal project for learning and experimentation use.
