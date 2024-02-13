'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''

# Define uma função que calcula a sequência de Fibonacci até o número informado pelo usuário
def fibonacci(limite):
  # Inicializando a sequência com os dois primeiros termos: 0 e 1
  sequencia = [0, 1]

  # Enquanto o último termo da sequência for menor que o limite, calcule o próximo termo como a soma dos dois anteriores, e o adicione à sequência
  while sequencia[-1] < limite:
    proximo = sequencia[-1] + sequencia[-2]
    sequencia.append(proximo)

  return sequencia

# Coleta número do usuário
num = int(input("Informe um número: "))

# Chama a função que calcula a sequência de fibonacci
sequencia = fibonacci(num)

# Verifica se o número informado pertence à sequência e informa ao usuário
if num in sequencia:
  print(f"O número {num} pertence à sequência de Fibonacci.")
else:
  print(f"O número {num} não pertence à sequência de Fibonacci.")
