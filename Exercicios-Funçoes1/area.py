def area(l, c):
    res = l * c
    print(f'A área de um terreno {l}x{c} é de {res}m²')

print("Controle de Terrenos")
print("-" * 20)
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura, comprimento)