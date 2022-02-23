numeros = [[], []]
for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
        numeros[0].sort()
    else:
        numeros[1].append(num)
        numeros[1].sort()
print("-=" * 35)
print(f'Os valores pares digitados foram {numeros[0]}')
print(f'Os valores impares digitados foram {numeros[1]}')
sair = input("ENTER para sair... ")
