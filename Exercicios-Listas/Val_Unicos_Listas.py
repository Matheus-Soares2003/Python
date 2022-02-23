valores = []
cont = 0
continuar = ''
while True:
    val = int(input("Digite um valor: "))
    if val not in valores:
        print("Valor adicionado com sucesso...")
        valores.append(val)
    else:
        print("Valor duplicado! Não vou adicionar...")
    continuar = str(input("Quer continuar? [S/N] "))
    if continuar in 'Nn':
        break
    cont = 0
print("=-" * 35)
valores.sort()
print(f'Você digitou os valores {valores}')
sair = input("ENTER para sair... ")
