from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot import convo_qa_chain, chat_history  # Asegúrate de que `chat_history` sea accesible

app = FastAPI()

class Query(BaseModel):
    input: str

@app.post("/query")
def get_response(query: Query):
    try:
        result = convo_qa_chain.invoke({
            "input": query.input,
            "chat_history": chat_history
        })
        response = result['output']
        if 'context' in result and result['context']:
            sources = set([doc['metadata']['source'] for doc in result['context']])
            source_info = ', '.join(sources)
        else:
            source_info = "No se encontraron fuentes relevantes."
        
        # Actualizar el historial de chat
        chat_history.append(("user", query.input))
        chat_history.append(("assistant", response))
        
        return {"response": response, "sources": source_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
