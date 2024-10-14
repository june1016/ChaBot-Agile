from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate

# Configurar el modelo de embeddings
embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Cargar la base de datos vectorial
persist_directory = './chroma_db'
vectorstore = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_model
)

# Configurar el modelo de lenguaje
llm = ChatOllama(
    model='llama3.2',
    temperature=0
)

# Definir el prompt para condensar la pregunta
condense_question_system_template = (
    "Given the following conversation and a follow-up question, "
    "rephrase the follow-up question to be a standalone question. "
    "Do not provide an answer yet."
)

condense_question_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", condense_question_system_template),
        ("user", "{chat_history}"),
        ("user", "{input}")
    ]
)

# Crear el retriever consciente del historial
history_aware_retriever = create_history_aware_retriever(
    llm,
    vectorstore.as_retriever(),
    condense_question_prompt
)

# Definir el prompt para la generación de respuestas
system_prompt = (
    "You are an expert assistant on Agile methodologies. "
    "Use the following context to answer the user's question. "
    "If you don't know the answer, say you don't know. "
    "Provide concise and precise answers.\n\n{context}"
)

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("user", "{chat_history}"),
        ("user", "{input}")
    ]
)

# Crear la cadena de generación de respuestas
qa_chain = create_stuff_documents_chain(llm, qa_prompt)

# Crear la cadena de recuperación
convo_qa_chain = create_retrieval_chain(
    history_aware_retriever,
    qa_chain
)

def main():
    print("Bienvenido al Chatbot sobre Metodologías Ágiles. Escribe 'salir' para terminar.")
    chat_history = []
    while True:
        query = input("\nPor favor, ingresa tu pregunta: ")
        if query.lower() in ['salir', 'exit', 'quit']:
            print("¡Hasta luego!")
            break

        # Ejecutar la cadena de consulta conversacional
        result = convo_qa_chain.invoke({
            "input": query,
            "chat_history": chat_history
        })

        print(f"Resultado completo: {result}")

        # Verificar la estructura de la respuesta y extraer la respuesta adecuadamente
        if isinstance(result, dict):
            if 'output' in result:
                response = result['output']
            elif 'answer' in result:
                response = result['answer']
            else:
                response = str(result)  # Convertir todo el resultado a string si no se encuentra una clave específica
        else:
            response = str(result)

        print(f"\nRespuesta:\n{response}")

        # Actualizar el historial de chat
        chat_history.append(("user", query))
        chat_history.append(("assistant", response))

if __name__ == "__main__":
    main()
