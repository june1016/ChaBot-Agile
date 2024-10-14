import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Directorio donde se encuentran los PDFs
DATA_DIR = './data'

def load_pdfs(data_dir):
    documents = []
    for file_name in os.listdir(data_dir):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(data_dir, file_name)
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            documents.extend(docs)
            print(f"Cargado {file_name} con {len(docs)} páginas.")
    return documents

if __name__ == "__main__":
    docs = load_pdfs(DATA_DIR)
    print(f"Total de documentos cargados: {len(docs)}")

    # Configurar el divisor de texto
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    # Dividir los documentos
    split_docs = text_splitter.split_documents(docs)
    print(f"Total de fragmentos después de dividir: {len(split_docs)}")

    # Configurar el modelo de embeddings
    embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    # Crear y persistir la base de datos vectorial
    persist_directory = './chroma_db'
    vectorstore = Chroma.from_documents(
        documents=split_docs,
        embedding=embedding_model,
        persist_directory=persist_directory
    )

    print("Fragmentos almacenados en la base de datos vectorial.")
