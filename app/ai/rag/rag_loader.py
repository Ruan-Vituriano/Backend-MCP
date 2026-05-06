import os

def carregar_documentos(pasta="data/docs"):
    documentos = []

    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".txt"):
            caminho = os.path.join(pasta, arquivo)

            with open(caminho, "r", encoding="utf-8") as f:
                texto = f.read()

                documentos.append({
                    "nome": arquivo,
                    "conteudo": texto
                })

    return documentos


def dividir_em_chunks(texto, tamanho=500, overlap=50):
    chunks = []
    
    inicio = 0
    while inicio < len(texto):
        fim = inicio + tamanho
        chunk = texto[inicio:fim]
        chunks.append(chunk)

        inicio += tamanho - overlap

    return chunks

def criar_base(documentos):
    base = []

    for doc in documentos:
        chunks = dividir_em_chunks(doc["conteudo"])

        for chunk in chunks:
            base.append({
                "texto": chunk,
                "fonte": doc["nome"]
            })

    return base

