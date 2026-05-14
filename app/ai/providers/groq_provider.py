from groq import Groq

from app.core.config import GROQ_API_KEY

from app.ai.rag.rag_service import buscar_contexto
from app.ai.rag.rag_loader import carregar_documentos, criar_base

client = Groq(api_key=GROQ_API_KEY)

_BASE_RAG = None


def _get_base_rag():
    global _BASE_RAG

    if _BASE_RAG is None:
        documentos = carregar_documentos()
        _BASE_RAG = criar_base(documentos)

    return _BASE_RAG


def gerar_resposta_groq(pergunta: str):

    base = _get_base_rag()

    contexto = buscar_contexto(pergunta, base)

    prompt = f"""
    Você é um assistente agrícola especializado em hortaliças.

    Use o contexto abaixo para responder da melhor forma possível.

    Contexto:
    {contexto}

    Pergunta:
    {pergunta}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente agrícola especializado em hortaliças."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4
    )

    return response.choices[0].message.content