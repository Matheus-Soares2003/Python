pessoas = list()
dados = []
maior = menor = 0
while True:
    dados.append(str(input("Nome: ").strip()))
    dados.append(float(input("Peso: ")))
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input("Continuar: [S/N] ")).strip()
    if continuar in 'Nn':
        break
print("-=" * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas')
maior = pessoas[0][1]
menor = pessoas[0][1]
print(f'O maior peso foi de {maior}Kg. Peso de ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
print(f'O menor peso foi de {menor}Kg.',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ',end='')
print()
sair = input("ENTER para sair... ")
