galera = []
pessoas = {}
media = soma = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input("Nome: "))
    pessoas['Sexo'] = str(input("Sexo: ")).strip().upper()[0]
    while pessoas['Sexo'] not in 'MmFf':
        print("ERRO! Por favor, digite somente M ou F.")
        pessoas['Sexo'] = str(input("Sexo: ")).strip().upper()[0]
    pessoas['Idade'] = int(input("Idade: "))
    soma = soma + pessoas['Idade']
    galera.append(pessoas.copy())
    continuar = str(input("Quer continuar? [S/N] ")).strip()[0]
    while continuar not in "SsNn":
        print("ERRO! Responda somente S ou N.")
        continuar = str(input("Quer continuar? [S/N] ")).strip()[0]
    if continuar in 'Nn':
        break

media = soma / len(galera)
print("-=" * 35)
print(f'A) Números de pessoas cadastradas: {len(galera)}')
print(f'B) A média de idade é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram ',end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f"{p['Nome']} ", end='')
print()
print(f'D) Pessoas com idade acima da média: ')
for p in galera:
    print("       ")
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
sair = input()