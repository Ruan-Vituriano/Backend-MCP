def buscar_contexto(pergunta, base):
    resultados = []

    for item in base:
        if pergunta.lower() in item["texto"].lower():
            resultados.append(item["texto"])

    return "\n".join(resultados[:3])