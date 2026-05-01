from app.ai.agent import gerar_resposta

def responder(pergunta: str, user_id: int):
    # futuramente você usa o user_id pra personalizar
    return gerar_resposta(pergunta)
