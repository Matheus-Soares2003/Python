matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range (0, 3):
    for j in range (0, 3):
        num = int(input(f'Digite um valor para [{i}, {j}]: '))
        matriz[i][j] = num

print("-=" * 35)
for i in range (0, 3):
    for j in range (0, 3):
        print(f'[{matriz[i][j]:^5}]',end=' ')
    print()
sair = input("ENTER para sair... ")