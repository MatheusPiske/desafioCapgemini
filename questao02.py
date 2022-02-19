# QUESTÃO 02

def incidencias(analise, lista):
    for i in analise:
        if i in senha:
            lista.append(i)

# Listas de verficação no sistema
incidenciasDigitos = []
incidenciasLetrasMinusculas = []
incidenciasLetrasMaiusculas = []
incidenciasCaracteresEspeciais = []

# Listas dos caracteres requisitados pelo site
caracteresEspeciais = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]
digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letrasAlfabetoMaiusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letrasAlfabetoMinusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
reiniciar = True

# INICIO DO PROGRAMA

while reiniciar == True:
    
    verificacao = True
    senha = input("INFORME QUAL É A SENHA A SER CADASTRADA NO SITE: ")
    caracteres = str(6 - len(senha))
    print("\n")

    if len(senha) < 6:
        print("Sua senha precisa ter, no mínimo, mais " + caracteres + " caracteres")
        verificacao = False

    incidencias(digitos, incidenciasDigitos)

    if len(incidenciasDigitos) == 0:
        print("Sua senha deve ter pelo menos um digito")
        verificacao = False

    incidencias(letrasAlfabetoMaiusculas, incidenciasLetrasMaiusculas)

    if len(incidenciasLetrasMaiusculas) == 0:
        print("Sua senha deve ter pelo menos uma letra maiúscula")
        verificacao = False

    incidencias(letrasAlfabetoMinusculas, incidenciasLetrasMinusculas)
        
    if len(incidenciasLetrasMinusculas) == 0:
        print("Sua senha deve ter pelo menos uma letra minúscula")
        verificacao = False

    incidencias(caracteresEspeciais, incidenciasCaracteresEspeciais)

    if len(incidenciasCaracteresEspeciais) == 0:
        print("Sua senha deve ter pelo menos um caracter especial. Dentre eles temos: !@#$%^&*()-+")
        verificacao = False

    if verificacao == True:
        print("Parabéns, a senha digitada atende aos padrões de segurança!")
    
    teste1 = True
    while teste1 == True:
        print("\n")
        resposta = input("Gostaria de reiniciar o programa? (S/N): ").lower()
        if resposta == "s":
            teste1 = False
            print("\n")
        elif resposta == "n":
            teste1 = False
            reiniciar = False
        else:
            print("Opção inválida! Digite 'S' ou 'N': ")

input("Pressione ENTER para fechar o programa")