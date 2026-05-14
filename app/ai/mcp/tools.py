def clima_atual(cidade: str) -> str:
    """Retorna o clima atual de uma cidade"""
    return f"O clima em {cidade} está quente, cerca de 32°C e seco."

def recomendacao_cultura(cultura: str) -> str:
    """Retorna recomendações de cultivo"""
    if cultura.lower() == "alface":
        return "A alface cresce melhor em clima ameno e solo úmido."
    
    return "Não tenho dados sobre essa cultura."

def diagnostico_sintomas(sintomas: str, cultura: str = "") -> str:
    """Sugere causas prováveis com base em sintomas"""
    sintomas_lower = sintomas.lower()
    cultura_lower = cultura.lower()

    if "amarel" in sintomas_lower and "folha" in sintomas_lower:
        return "Possiveis causas: falta de nitrogenio, excesso de agua ou baixa luminosidade. Verifique irrigacao e adubacao."
    if "mancha" in sintomas_lower or "pinta" in sintomas_lower:
        return "Possiveis causas: fungos (mildio, septoriose) ou bacteriose. Reduza umidade nas folhas e melhore ventilacao."
    if "murcha" in sintomas_lower or "murch" in sintomas_lower:
        return "Possiveis causas: estresse hidrico, podridao de raiz ou calor excessivo. Cheque drenagem e irrigacao."
    if "praga" in sintomas_lower or "inset" in sintomas_lower:
        return "Possiveis causas: pulgao, mosca-branca ou trips. Inspecione a face inferior das folhas."

    if cultura_lower:
        return f"Sintomas pouco especificos para {cultura_lower}. Envie mais detalhes (folha, haste, raiz) e condicoes do cultivo."
    return "Sintomas pouco especificos. Envie mais detalhes (folha, haste, raiz) e condicoes do cultivo."

def controle_pragas(praga: str, cultura: str = "") -> str:
    """Retorna manejo integrado de pragas"""
    praga_lower = praga.lower()
    cultura_lower = cultura.lower()

    if "pulgao" in praga_lower:
        return "Manejo: use jato de agua, controle biologico (joaninhas) e oleo de neem em baixa concentracao."
    if "mosca" in praga_lower:
        return "Manejo: use armadilhas adesivas amarelas, controle de plantas hospedeiras e neem."
    if "trips" in praga_lower:
        return "Manejo: remova folhas afetadas, use armadilhas azuis e mantenha umidade adequada."
    if "lagarta" in praga_lower:
        return "Manejo: cata manual, Bacillus thuringiensis e rotacao de culturas."

    if cultura_lower:
        return f"Sem protocolo especifico para {cultura_lower}. Informe sintomas e nivel de infestacao."
    return "Sem protocolo especifico. Informe sintomas e nivel de infestacao."

def calculo_adubacao(cultura: str, area_m2: float, tipo_solo: str = "") -> str:
    """Calcula adubacao basica por area"""
    if area_m2 <= 0:
        return "Area invalida. Informe a area em m2 maior que zero."

    doses_g_m2 = {
        "alface": 60,
        "tomate": 120,
        "coentro": 40
    }
    cultura_lower = cultura.lower()
    dose = doses_g_m2.get(cultura_lower, 80)

    fator = 1.0
    tipo_solo_lower = tipo_solo.lower()
    if "arenoso" in tipo_solo_lower:
        fator = 1.2
    elif "argiloso" in tipo_solo_lower:
        fator = 0.9

    dose_total_kg = (dose * fator * area_m2) / 1000
    return (
        f"Adubacao base sugerida: NPK 5-10-5 a {dose * fator:.0f} g/m2. "
        f"Para {area_m2:.1f} m2: {dose_total_kg:.2f} kg. Ajuste conforme analise de solo."
    )

