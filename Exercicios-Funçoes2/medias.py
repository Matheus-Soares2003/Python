def med_aritmetica(num):
    return sum(num) / len(num)


def med_harmonica(num):
    soma = 0
    for c in num:
        soma = soma + (1 / c)
    media_h = len(num) / soma
    return media_h


def med_geometrica(num):
    cont = 0
    media_g = 1
    for v in num:
        num[cont] = v ** (1 / len(num))
        media_g = media_g * num[cont]
        cont += 1
    
    return media_g

    
    
numeros = [3, 6, 9]
media = med_aritmetica(numeros)
print(f"{media:.2f}")




