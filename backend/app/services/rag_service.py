import chromadb
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline
import os

# Initialize ChromaDB
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))


chroma_path = os.path.join(BASE_DIR, "chroma_db")
print(chroma_path)
chroma_client = chromadb.PersistentClient(path=chroma_path)
collection = chroma_client.get_collection("hr_knowledge")

# Embedding model (FREE)
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Local LLM (FREE)
qa_pipeline = pipeline(
    "text-generation",
    model="google/flan-t5-base",   # lightweight & good for QA
    max_length=512
)


def ask_question(question):

    # Step 1: Convert question to embedding
    query_embedding = embedding_model.embed_query(question)

    # Step 2: Search in ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    # Step 3: Prepare context
    documents = results["documents"][0]
    context = "\n\n".join(documents)

    # Step 4: Create prompt
    prompt = f"""
    Answer the question based on the context below.

    Context:
    {context}

    Question:
    {question}
    """

    # Step 5: Generate answer using HuggingFace
    response = qa_pipeline(prompt)
    return response[0]["generated_text"]