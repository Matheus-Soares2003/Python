num = []
maior = 0
menor = 0
posMaior = []
posMenor = []
for c in range(0, 5):
    num.append(int(input(f'Valor da posição {c}: ')))
    if c == 0:
        menor = num[c]
        maior = num[c]
    else:
        if num[c] > maior:
            maior = num[c]   
        if num[c] < menor:
            menor = num[c]

print("=-" * 30)
print(f'Você digitou os valores {num}')
print(f'O maior valor é {maior} e ele está nas posições ',end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor é {menor} e ele está nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')
print()
sair = input("ENTER para sair... ")
