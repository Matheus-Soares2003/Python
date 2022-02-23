jogador = {}
gols = []
total = 0
jogador['Nome'] = str(input("Nome do jogador: "))
Partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
for c in range(0, Partidas):
    golsTemp = int(input(f'Quantos gols na partida {c + 1}? '))
    total = total + golsTemp
    gols.append(golsTemp)
jogador['Gols'] = gols[:]
jogador['Total'] = total
print("-=" * 35)
print(jogador)
print("-=" * 35)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print("-=" * 35)
print(f'O jogador {jogador["Nome"]} jogou {Partidas} partidas.')
for c in range(0, Partidas):
    print(f'    => Na partida {c + 1}, fez {gols[c]} gols')
print(f'Foi um total de {total} gols.')
