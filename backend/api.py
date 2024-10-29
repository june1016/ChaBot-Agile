from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot import get_response  # Importar la función desde chatbot.py

app = FastAPI()

class Query(BaseModel):
    input: str

@app.post("/query")
def query_chatbot(query: Query):
    try:
        response, sources = get_response(query.input)
        return {"response": response, "sources": sources}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
