lista = []
pares = []
impares = []
while True:
    val = int(input("Digite um valor: "))
    lista.append(val)
    if val % 2 == 0:
        pares.append(val)
    else:
        impares.append(val)
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in 'Nn':
        break
print("-=" * 35)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
sair = input("ENTER para sair... ")