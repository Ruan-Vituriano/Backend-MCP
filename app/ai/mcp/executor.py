from app.ai.mcp.tools import (
    clima_atual,
    recomendacao_cultura,
    diagnostico_sintomas,
    controle_pragas,
    calculo_adubacao
)

def executar_tool(nome: str, args: dict):
    if nome == "clima_atual":
        return clima_atual(**args)

    elif nome == "recomendacao_cultura":
        return recomendacao_cultura(**args)

    elif nome == "diagnostico_sintomas":
        return diagnostico_sintomas(**args)

    elif nome == "controle_pragas":
        return controle_pragas(**args)

    elif nome == "calculo_adubacao":
        return calculo_adubacao(**args)

    return "Tool não encontrada"
