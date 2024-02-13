'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

# Coletando do usuário a string a ser invertida
string = input("Digite a string que você quer inverter: ")

# Variável vazia para armazenar a string invertida
invertida = ''

# Percorrendo os caracteres da string original, de trás para frente
for i in range(len(string) - 1, -1, -1):
    invertida += string[i]

# Exibindo a string invertida
print(f"A string invertida é: {invertida}")
