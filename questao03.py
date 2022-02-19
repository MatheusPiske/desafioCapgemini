# QUESTÃO 03

from itertools import permutations

palavra = input("Digite a palavra a ser analisada: ")
pedacos_da_palavra = []
pares_de_anagramas = []

for y in range(len(palavra)):
    for i in range(len(palavra)):
        if len(palavra[i:i+y]) == y:
            pedacos_da_palavra.append(palavra[i:i+y])


for pedaco in pedacos_da_palavra:
    if len(pedaco) == 1:
        if pedacos_da_palavra.count(pedaco) > 1 and [pedaco, pedaco] not in pares_de_anagramas:
            pares_de_anagramas.append([pedaco, pedaco])
    else:
        pedaco_permutacoes = [''.join(anagrama)
                              for anagrama in permutations(pedaco)]
        for permutacao in pedaco_permutacoes:
            if permutacao in pedacos_da_palavra and permutacao != pedaco and [permutacao, pedaco] not in pares_de_anagramas:
                pares_de_anagramas.append([pedaco, permutacao])

print(f"\nOs pares de anagramas da palavra {palavra} são: {pares_de_anagramas}")
print(f"O número de pares de substrings que são anagramas é: {len(pares_de_anagramas)}")
input()