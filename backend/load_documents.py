import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

# Directorio donde se encuentran los PDFs
DATA_DIR = './data'

def load_pdfs(data_dir):
    documents = []
    for file_name in os.listdir(data_dir):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(data_dir, file_name)
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            # Añadir el nombre del archivo como metadato "source"
            for doc in docs:
                doc.metadata["source"] = file_name
            documents.extend(docs)
            print(f"Cargado {file_name} con {len(docs)} páginas.")
    return documents

if __name__ == "__main__":
    try:
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

        # Configurar el modelo de embeddings utilizando HuggingFace
        print("Iniciando configuración del modelo de embeddings...")
        embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
        print("Modelo de embeddings configurado.")

        # Crear el vectorstore con Chroma
        print("Creando el vectorstore de Chroma...")
        persist_directory = './chromadb'
        collection_name = 'agile_documents'

        vectorstore = Chroma(
            embedding_function=embedding_model,
            persist_directory=persist_directory,
            collection_name=collection_name
        )

        # Añadir los documentos al vectorstore
        print("Actualizando la colección en Chroma...")
        vectorstore.add_documents(split_docs)
        vectorstore.persist()
        print("Fragmentos almacenados en la base de datos vectorial correctamente.")

    except Exception as e:
        print(f"Error al cargar y almacenar documentos: {e}")
