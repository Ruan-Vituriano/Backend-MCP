docs = [
    "Alface cresce melhor em clima ameno e solo úmido.",
    "Tomate precisa de sol pleno e irrigação controlada.",
    "Coentro prefere clima mais fresco e solo bem drenado."
]

def buscar_contexto(pergunta: str):
    resultados = []

    for doc in docs:
        if any(palavra in doc.lower() for palavra in pergunta.lower().split()):
            resultados.append(doc)

    return "\n".join(resultados) if resultados else "Sem contexto relevante."
