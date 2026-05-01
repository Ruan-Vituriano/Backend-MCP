from google import genai
from app.core.config import GEMINI_API_KEY
from app.ai.rag.rag_service import buscar_contexto

client = genai.Client(api_key=GEMINI_API_KEY)

def gerar_resposta(pergunta: str):
    contexto = buscar_contexto(pergunta)

    prompt = f"""
    Você é um assistente agrícola.

    Contexto:
    {contexto}

    Pergunta:
    {pergunta}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
