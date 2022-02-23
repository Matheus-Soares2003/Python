from random import randint

def sorteia(n):
    print("Sorteando 5 valores da lista: ", end='')
    for c in range(0, 5):
        num = randint(1, 10)
        n.append(num)
    for v in n:
        print(f'{v} ', end='')
    print("PRONTO!")

def somaPar(n):
    s = 0
    for v in n:
        if v % 2 == 0:
            s = s + v
    print(f'Somando os valores pares de {n} temos {s}')   


numeros = []
sorteia(numeros)
somaPar(numeros)
