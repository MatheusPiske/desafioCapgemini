# QUESTÃO 01

n = int(input("Escolha o valor de 'n' para montar a escada: "))
passagens = 1
caracter = "*"

for i in range(n):
    espaco = " " * (n - passagens)
    espaco = espaco + caracter * passagens
    passagens = passagens + 1
    print(espaco)

input()            