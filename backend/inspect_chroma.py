from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

# Configurar el modelo de embeddings
embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Cargar la base de datos vectorial con el mismo nombre de colección
persist_directory = './chromadb'
collection_name = "agile_documents"  # Debe coincidir con el nombre usado en load_documents.py

vectorstore = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_model,
    collection_name=collection_name
)

# Obtener todos los documentos y metadatos
print("Obteniendo documentos de la colección...")
docs = vectorstore.get()["documents"]
metadatas = vectorstore.get()["metadatas"]

print(f"Total de documentos en la colección: {len(docs)}")

for i, doc in enumerate(docs):
    source = metadatas[i].get('source', 'Desconocido')
    print(f"Documento: {source}")
    print(f"Contenido (resumido): {doc[:100]}...\n")
