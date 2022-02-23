def med_aritmetica(num):
    return sum(num) / len(num)


def med_harmonica(num):
    soma = 0
    for c in num:
        soma = soma + (1 / c)
    media_h = len(num) / soma
    return media_h


def med_geometrica(num):
    lista_num = num.copy()
    cont = 0
    media_g = 1
    for v in num:
        lista_num[cont] = v ** (1 / len(num))
        media_g = media_g * lista_num[cont]
        cont += 1
    
    return media_g

    
    
numeros = [12, 4, 8, 16]
ma = med_aritmetica(numeros)
mh = med_harmonica(numeros)
mg = med_geometrica(numeros)

print(f"""Média Aritmética de {numeros} -> {ma:.2f}
Média Geométrica de {numeros} -> {mg:.2f}
Média Harmônica de {numeros} -> {mh:.2f}""")





