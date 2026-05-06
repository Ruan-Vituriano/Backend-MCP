from google import genai
from app.core.config import GEMINI_API_KEY
from app.ai.rag.rag_service import buscar_contexto
from app.ai.rag.rag_loader import carregar_documentos, criar_base
from app.ai.mcp.tools import clima_atual, recomendacao_cultura
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
    if contexto:
        print("[RAG] Contexto encontrado:\n" + contexto)
    else:
        print("[RAG] Nenhum contexto encontrado.")

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
            "tools": [clima_atual, recomendacao_cultura]
        }
    )
    
    return response.text
