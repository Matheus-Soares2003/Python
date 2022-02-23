palavras = ('Amendoim', 'Batata','Desinstalar','Pano','Papel','Impressora','Cano','Roupa','Sapato','Guitarra')

for c in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[c].upper()} temos', end=' ')
    for i in range(0, len(palavras[c])):
        if palavras[c][i].lower() in 'aeiou':
            print(palavras[c][i].lower(), end=' ')   
sair = input("ENTER para sair... ")
    
    