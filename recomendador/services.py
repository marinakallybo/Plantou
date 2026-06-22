def calcular_pontuacao(cultura, temperatura, solo, umidade):
    pontuacao = 0
    motivos = []

    if cultura.temperatura_minima <= temperatura <= cultura.temperatura_maxima:
        pontuacao += 40
        motivos.append("A temperatura informada está dentro da faixa ideal.")
    else:
        motivos.append("A temperatura informada está fora da faixa ideal.")

    if cultura.solo_ideal.lower() == solo.lower():
        pontuacao += 30
        motivos.append("O tipo de solo é compatível.")
    else:
        motivos.append("O tipo de solo não é o mais indicado.")

    if cultura.umidade_ideal.lower() == umidade.lower():
        pontuacao += 30
        motivos.append("A umidade informada é adequada.")
    else:
        motivos.append("A umidade informada não é a mais adequada.")

    return pontuacao, motivos


def recomendar_culturas(culturas, temperatura, solo, umidade):
    recomendacoes = []

    for cultura in culturas:
        pontuacao, motivos = calcular_pontuacao(cultura, temperatura, solo, umidade)

        if pontuacao >= 40:
            recomendacoes.append({
            "cultura": cultura,
            "pontuacao": pontuacao,
            "motivos": motivos
        })

    recomendacoes_ordenadas = sorted(
        recomendacoes,
        key=lambda item: item["pontuacao"],
        reverse=True
    )

    return recomendacoes_ordenadas