# contas de dias de faturamento

import json


def faturamento_diario():
    # Abrir e ler o arquivo JSON
    with open("dados.json", "r") as file:
        dados = json.load(file)  # Aqui, 'dados' será uma lista de dicionários

    # Extrair valores de faturamento
    faturamento = [item["valor"] for item in dados]

    # Remover dias sem faturamento (não haverá 0, mas é bom ter essa verificação)
    faturamento_validos = [valor for valor in faturamento if valor > 0]

    # Menor e maior valor de faturamento
    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)

    # Cálculo da média
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)

    # Dias com faturamento acima da média
    dias_acima_da_media = len(
        [valor for valor in faturamento_validos if valor > media_mensal]
    )

    print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
    print(f"Número de dias com faturamento superior à média: {dias_acima_da_media}")


# Chamada da função para testar
faturamento_diario()
