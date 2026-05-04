from google import genai
from app.core.config import GEMINI_API_KEY
from app.ai.rag.rag_service import buscar_contexto
from app.ai.mcp.registry import clima_atual, recomendacao_cultura
from app.ai.mcp.executor import executar_tool

client = genai.Client(api_key=GEMINI_API_KEY)

def gerar_resposta(pergunta: str):
    contexto = buscar_contexto(pergunta)

    prompt = f"""
    Você é um assistente agrícola.

    Use ferramentas quando necessário.

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

    # 🔥 Detectar chamada de função
    parts = response.candidates[0].content.parts

    for part in parts:
        if hasattr(part, "function_call"):
            nome = part.function_call.name
            args = part.function_call.args

            resultado = executar_tool(nome, args)

            final = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""
                Pergunta: {pergunta}

                Resultado da função:
                {resultado}

                Gere a resposta final.
                """
            )

            return final.text

    return response.text
