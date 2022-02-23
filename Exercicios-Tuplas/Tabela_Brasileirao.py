def linha():
    print('-=' * 10)

times = ('Palmeiras','Atlético-MG','Fortaleza','Bragantino','Athletico-PR','Flamengo','Ceará','Atlético-GO','Bahia','Corinthians','Fluminense','Santos','Juventude','Internacional','Cuiabá','Sport','São Paulo','América-MG','Grêmio','Chapecoense')

linha()
print(f'Lista de times do Brasileirão: {times}')
linha()
print(f'Os 5 primeiros são: {times[0:5]}')
linha()
print(f'Os 4 últimos são: {times[len(times) - 4:len(times)]}')
linha()
print(f'Em ordem alfabética: {sorted(times)}')
linha()
print(f'A chapecoense está em {times.index("Chapecoense") + 1}º\n')
sair = input("ENTER para sair... ")
