import re

_STOPWORDS = {
    "a", "o", "os", "as", "um", "uma", "uns", "umas",
    "de", "do", "da", "dos", "das", "para", "por", "com",
    "em", "no", "na", "nos", "nas", "que", "e", "ou",
    "qual", "quais", "como", "quando", "onde", "porque",
    "minima", "minimo", "maxima", "maximo"
}

def _normalizar(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    tokens = [t for t in texto.split() if t and t not in _STOPWORDS]
    return tokens

def buscar_contexto(pergunta, base, top_k=3):
    termos = _normalizar(pergunta)
    if not termos:
        return ""

    scored = []
    for item in base:
        texto = item["texto"].lower()
        score = sum(1 for t in termos if t in texto)
        if score > 0:
            scored.append((score, item["texto"]))

    scored.sort(key=lambda x: x[0], reverse=True)
    return "\n".join([t for _, t in scored[:top_k]])