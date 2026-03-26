import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader


def load_documents(path):
    documents = []

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if file.endswith('.pdf'):
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())

        elif file.endswith('.text'):
            loader = TextLoader(file_path)
            documents.extend(loader.load())

    print(f"Loaded {len(documents)} documents")
    return documents


