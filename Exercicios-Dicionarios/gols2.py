gols = []
jogador = {}
time = []
while True:
    jogador.clear()
    gols.clear()
    total = 0
    jogador['Nome'] = str(input("Nome do jogador: "))
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, partidas):
        golsTemp = int(input(f"Quantos gols na partida {c + 1}: "))
        total = total + golsTemp
        gols.append(golsTemp)
    jogador['Gols'] = gols[:]
    jogador['Total'] = total
    time.append(jogador.copy())
    continuar = str(input("Quer continuar? [S/N] ")).strip()[0]
    if continuar in 'Nn':
        break
print("-=" * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print("-" * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    mostrar = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if mostrar == 999:
        break
    if mostrar >= len(time):
          print(f'ERRO! Não existe jogador com código {mostrar}')
    else:
       print(f'-- Levantamento do jogador {time[mostrar]["Nome"]:}')
       for i, g in enumerate(time[mostrar]['gols']):
           print(f'     No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
        
