lista = []
cont = 0
while True:
    lista.append(int(input("Digite um valor: ")))
    cont += 1
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in 'Nn':
        break
lista.sort(reverse=True)
print("-=" * 35)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado!")
sair = input("ENTER para sair... ")