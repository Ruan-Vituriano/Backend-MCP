def clima_atual(cidade: str) -> str:
    # depois você conecta com API real
    return f"O clima em {cidade} está quente, cerca de 32°C e seco."

def recomendacao_cultura(cultura: str) -> str:
    if cultura.lower() == "alface":
        return "A alface cresce melhor em clima ameno e solo úmido."
    
    if cultura.lower() == "coentro":
        return "O coentro prefere clima fresco e solo bem drenado."

    return "Não tenho dados suficientes sobre essa cultura."
