# QUESTÃO 01

verificador = True
while verificador == True:
    
    n = input("Escolha o valor de 'n' para montar a escada: ")
    passagens = 1
    caracter = "*"

    if n.isnumeric() == True:
        for i in range(int(n)):
            espaco = " " * (int(n) - passagens)
            espaco = espaco + caracter * passagens
            passagens = passagens + 1
            print(espaco)
            
            verificador = False
    else: 
        print("O valor indicado precisa ser inteiro! \n")

input()            