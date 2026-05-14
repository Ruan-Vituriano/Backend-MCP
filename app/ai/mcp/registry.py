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
    },
    {
        "name": "diagnostico_sintomas",
        "description": "Sugere causas provaveis com base nos sintomas",
        "parameters": {
            "type": "object",
            "properties": {
                "sintomas": {"type": "string"},
                "cultura": {"type": "string"}
            },
            "required": ["sintomas"]
        }
    },
    {
        "name": "controle_pragas",
        "description": "Retorna manejo integrado de pragas",
        "parameters": {
            "type": "object",
            "properties": {
                "praga": {"type": "string"},
                "cultura": {"type": "string"}
            },
            "required": ["praga"]
        }
    },
    {
        "name": "calculo_adubacao",
        "description": "Calcula adubacao basica por area",
        "parameters": {
            "type": "object",
            "properties": {
                "cultura": {"type": "string"},
                "area_m2": {"type": "number"},
                "tipo_solo": {"type": "string"}
            },
            "required": ["cultura", "area_m2"]
        }
    }
]
