num = 0
cont = 1
while True:
    num = int(input("Quer ver a tabuada de qual valor? "))
    print("-="*30)
    if num < 0:
        break
    while cont <= 10:
        print(f"{num} x {cont} = {num * cont}")
        cont += 1
    cont = 0
sair = input("ENTER para sair... ")