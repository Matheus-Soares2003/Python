import pandas as pd

filmes = []
df_filmes = pd.read_csv('filmes.csv', sep=';', encoding='ISO-8859-1')
filmes.append(df_filmes.values)
print(df_filmes.values)

with open('filmes.txt', 'w') as arquivo:
    for l in range(df_filmes.shape[0]):
        for c in range(df_filmes.shape[1]):
            if c == 2:
                arquivo.write(f'{df_filmes.values[l][c]}\n')

arquivo.close()


