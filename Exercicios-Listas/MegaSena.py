from time import sleep
from random import randint
jogos = []
numeros = []
quant = int(input("Quantos jogos você quer que eu sorteie? "))
print(f"-=-=-=  SORTEANDO {quant} JOGOS  -=-=-=")
for c in range(0, quant):
    cont = 0
    while cont < 6:
        num = randint(1, 61)
        if num not in numeros:
            numeros.append(num)
            numeros.sort()
            cont += 1
    jogos.append(numeros[:])
    numeros.clear()
    sleep(1)
    print(f'Jogo {c + 1}: {jogos[c]}')
print("-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=")
print()
sair = input("ENTER para sair... ")
