from google import genai
from app.core.config import GEMINI_API_KEY
from app.ai.rag.rag_service import buscar_contexto
from app.ai.mcp.tools import clima_atual, recomendacao_cultura
from app.ai.mcp.executor import executar_tool

client = genai.Client(api_key=GEMINI_API_KEY)

def gerar_resposta(pergunta: str):
    contexto = buscar_contexto(pergunta)

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
