'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
'''

def calc_faturamento(faturamento):
    # A maior/menor ocorrência levando em conta o valor
    menor_valor = min(faturamento, key=lambda d: d["valor"])["valor"]
    maior_valor = max(faturamento, key=lambda d: d["valor"])["valor"]

    # O dia para cada ocorrência em faturamento em que o valor seja o maior/menor valor
    dias_menor = [d["dia"] for d in faturamento if d["valor"] == menor_valor]
    dias_maior = [d["dia"] for d in faturamento if d["valor"] == maior_valor]

    return menor_valor, maior_valor, dias_menor, dias_maior

def calc_media(faturamento):
    # Calculando a média mensal de faturamento
    media = sum(d["valor"] for d in faturamento) / len(faturamento)

    return media

def main(dados):
    # Filtrando os dias cujo faturamento é maior que 0 (ou seja, quando houve faturamento)
    faturamento = [d for d in dados if d["valor"] > 0]

    #Chama as funções que calculam o faturamento e a média
    menor_valor, maior_valor, dias_menor, dias_maior = calc_faturamento(faturamento)
    media = calc_media(faturamento)

    # Contando o número de dias em que o faturamento foi superior à média, e quais foram esses dias
    dias_acima = [d["dia"] for d in faturamento if d["valor"] > media]
    num_dias_acima = len(dias_acima)

    # Exibindo os resultados
    print(f"O menor faturamento ocorrido foi de R$ {menor_valor:.2f}, no dia {''.join(map(str, dias_menor))}.")
    print(f"O maior faturamento ocorrido foi de R$ {maior_valor:.2f}, no dia {''.join(map(str, dias_maior))}")
    print(f"Em {num_dias_acima} o faturamento diário foi superior à média mensal. Especificamente nos dias {', '.join(map(str, dias_acima))}")



