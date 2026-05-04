from app.ai.mcp.tools import clima_atual, recomendacao_cultura

def executar_tool(nome: str, args: dict):
    if nome == "clima_atual":
        return clima_atual(**args)

    elif nome == "recomendacao_cultura":
        return recomendacao_cultura(**args)

    return "Tool não encontrada"
