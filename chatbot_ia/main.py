from fastapi import FastAPI
from pydantic import BaseModel
from app.chatbot import generate_response  # ajuste o import se necessário

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/chat")
def chat_endpoint(prompt: Prompt):
    resposta = generate_response(prompt.prompt)
    return {"response": resposta}
