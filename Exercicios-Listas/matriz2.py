matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaJ = 0
somaPar = 0
maior = 0
for i in range (0, 3):
    for j in range (0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
        if matriz[i][j] % 2 == 0:
            somaPar = somaPar + matriz[i][j]
        if j == 2:
            somaJ = somaJ + matriz[i][j]
        if i == 1:
            if j == 0:
                maior = matriz[i][j]
            elif matriz[i][j] > maior:
                maior = matriz[i][j]

print("-=" * 30)
for i in range (0, 3):
    for j in range (0, 3):
        print(f'[{matriz[i][j]:^5}]',end=' ')
    print()
print("-=" * 30)
print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaJ}')
print(f'O maior valor da segunda linha é {maior}')
sair = input("ENTER para sair... ")