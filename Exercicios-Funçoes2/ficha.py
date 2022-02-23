def ficha(j="<desconhecido>", g=0):
    print(f'O jogador {j} fez {g} gols no campeonato')

jogador = str(input("Nome do Jogador: "))
gols = str(input("Número de gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(g=gols)
else:
    ficha(jogador, gols)
