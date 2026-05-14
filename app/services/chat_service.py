from app.ai.providers.llm_provider import gerar_resposta

def responder(pergunta: str, user_id: int):
    return gerar_resposta(pergunta)
