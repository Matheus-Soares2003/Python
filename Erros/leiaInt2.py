def leiaInt(msg):
    ok = False
    while not ok:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print("\033[0;31mO usuário preferiu não digitar.\033[m")
            ok = True
            num = 0 
        except:
            print("\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m")
        else:
            ok = True
    return num

def leiaFloat(msg):
    ok = False
    while not ok:
        try:
            num = float(input(msg))
        except KeyboardInterrupt:
            print("\033[0;31mO usuário preferiu não digitar.\033[m")
            ok = True
            num = 0 
        except:
            print("\033[0;31mERRO! Por favor, digite um número real válido.\033[m")
        else:
            ok = True
    return num

#Programa Principal
n1 = leiaInt("Digite um número: ")
n2 = leiaFloat("Digite um número Real: ")
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
