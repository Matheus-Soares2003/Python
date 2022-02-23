from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'OS valores sorteados foram: {numeros}')
print(f'O maior valor é {sorted(numeros)[len(numeros) - 1]}!')
print(f'O menor valor é {sorted(numeros)[0]}!')
sair = input("ENTER para sair... ")
