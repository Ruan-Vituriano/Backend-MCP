def clima_atual(cidade: str) -> str:
    """Retorna o clima atual de uma cidade"""
    return f"O clima em {cidade} está quente, cerca de 32°C e seco."

def recomendacao_cultura(cultura: str) -> str:
    """Retorna recomendações de cultivo"""
    if cultura.lower() == "alface":
        return "A alface cresce melhor em clima ameno e solo úmido."
    
    return "Não tenho dados sobre essa cultura."

