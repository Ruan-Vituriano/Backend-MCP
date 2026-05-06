from google import genai
from app.core.config import GEMINI_API_KEY
from app.ai.rag.rag_service import buscar_contexto
from app.ai.rag.rag_loader import carregar_documentos, criar_base
from app.ai.mcp.tools import (
    clima_atual,
    recomendacao_cultura,
    diagnostico_sintomas,
    controle_pragas,
    calculo_adubacao
)
from app.ai.mcp.executor import executar_tool

client = genai.Client(api_key=GEMINI_API_KEY)
_BASE_RAG = None

def _get_base_rag():
    global _BASE_RAG
    if _BASE_RAG is None:
        documentos = carregar_documentos()
        _BASE_RAG = criar_base(documentos)
    return _BASE_RAG

def gerar_resposta(pergunta: str):
    base = _get_base_rag()
    contexto = buscar_contexto(pergunta, base)

    prompt = f"""
    Você é um assistente agrícola.

    Use ferramentas quando necessário.
    O RAG também pode fornecer contexto adicional para perguntas específicas, então use isso para melhorar suas respostas.
    
    Contexto:
    {contexto}

    Pergunta:
    {pergunta}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "tools": [
                clima_atual,
                recomendacao_cultura,
                diagnostico_sintomas,
                controle_pragas,
                calculo_adubacao
            ]
        }
    )
    
    return response.text
