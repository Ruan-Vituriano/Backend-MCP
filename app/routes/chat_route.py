from fastapi import APIRouter
from app.services.chat_service import responder

router = APIRouter()

@router.post("/chat")
def chat(data: dict):
    pergunta = data.get("pergunta")
    user_id = data.get("user_id")

    resposta = responder(pergunta, user_id)

    return {"resposta": resposta}
