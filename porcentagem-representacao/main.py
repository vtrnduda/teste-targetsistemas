''' Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

Para este problema, irei optar por resolver com a biblioteca Pandas, para fins de destacar minhas habilidades.
'''

import pandas as pd

# Dataframe para armazenar os dados
df = pd.DataFrame({
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}, index=[0])

# Valor total do faturamento
total = df.sum().sum()
print(total)

#fórmula da porcentagem: (parte/todo) * 100
percentual = ((df / total) * 100).round(2)

# Exibindo os resultados
print(f'O valor total de faturamento foi: R$ {total:.2f}')
print('O percentual de representação de cada estado foi:')
print(percentual)

#Salvar em um csv para futuras avaliações e tomadas de decisão
path = 'percentual.csv'
percentual.to_csv(path, index=False, sep=';')

print(f'Seu resultado foi salvo com sucesso no arquivo "{path}"')








