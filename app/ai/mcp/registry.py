tools = [
    {
        "name": "clima_atual",
        "description": "Retorna o clima atual de uma cidade",
        "parameters": {
            "type": "object",
            "properties": {
                "cidade": {"type": "string"}
            },
            "required": ["cidade"]
        }
    },
    {
        "name": "recomendacao_cultura",
        "description": "Retorna recomendações de cultivo",
        "parameters": {
            "type": "object",
            "properties": {
                "cultura": {"type": "string"}
            },
            "required": ["cultura"]
        }
    }
]
