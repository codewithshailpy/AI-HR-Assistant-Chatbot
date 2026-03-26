import chromadb
from langchain_openai import OpenAIEmbeddings
from document_loader import load_documents
from chunking import chunk_documents
import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Step 1: Load documents
documents = load_documents(
    "data/raw_docs/hr"
)

# Step 2: Chunk documents
chunks = chunk_documents(documents)

# Step 3: Setup embeddings
embedding_model = OpenAIEmbeddings(
    openai_api_key=OPENAI_API_KEY
)

# Step 4: Setup ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="hr_knowledge"
)

# Step 5: Store embeddings
for i, chunk in enumerate(chunks):

    embedding = embedding_model.embed_query(
        chunk.page_content
    )

    collection.add(
        documents=[chunk.page_content],
        embeddings=[embedding],
        ids=[str(i)]
    )

print("✅ Documents embedded and stored in ChromaDB")