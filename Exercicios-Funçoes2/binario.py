def toBinary(num):
    resto = ''
    while num > 1:
        resto += str(num % 2)
        num = num // 2
    resto += "1"
    return resto[::-1]


def toDecimal(binum):
    soma = 0
    pot = len(binum) - 1
    for c in range(len(binum)):
        soma += int(binum[c]) * pow(2, pot)
        pot -= 1
    return soma


for c in range(20):
    binario = str(input("Binario: "))
    print(f"{binario} -> {toDecimal(binario)}")


for i in range(20):
    dec = int(input("Decimal: "))
    print(f"{dec} -> {toBinary(dec)}")