def leiaInt(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric()==False:
            print("\033[0;31mERRO! Digite um número válido.\033[m")
        else:
            num = int(num)
            break
    return num

n = leiaInt("Digite um número: ")
print(f'Você acabou de digitar o número {n}')
