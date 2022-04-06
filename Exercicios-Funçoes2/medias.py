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
    for v in lista_num:
        lista_num[cont] = v ** (1 / len(num))
        media_g = media_g * lista_num[cont]
        cont += 1
    
    return media_g


def desvio_medio(num):
    lista_num = num.copy()
    media = med_aritmetica(lista_num)
    soma = 0
    for v in lista_num:
        soma = soma + (abs(v - media))
    d = soma / len(lista_num)
    return d


def variancia(num):
    lista_num = num.copy()
    soma = 0
    media = med_aritmetica(lista_num)
    for v in lista_num:
        soma = soma + ((v - media) ** 2)
    v = soma / len(lista_num)
    return v


def desvio_padrao(num):
    return variancia(num) ** 0.5 #retorna a raiz quadrada da variancia de num

#-------Teste das funções-------#
    
numeros = [7, 8, 1, 3, 2, 5, 2]
ma = med_aritmetica(numeros)
mh = med_harmonica(numeros)
mg = med_geometrica(numeros)
dm = desvio_medio(numeros)
var = variancia(numeros)
dp = desvio_padrao(numeros)

print(f"""Média Aritmética de {numeros} -> {ma:.2f}
Média Geométrica de {numeros} -> {mg:.2f}
Média Harmônica de {numeros} -> {mh:.2f}
Desvio Médio -> {dm:.2f}
Variânica -> {var:.2f}
Desvio Padrão -> {dp:.2f}""")
