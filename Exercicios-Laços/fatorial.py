num = int(input("Digite um número para saber seu fatorial: "))
fat = 1
print(f"Calculando {num}! = ", end='')

while num > 0:
    print(f"{num}", end='')
    print(" x " if num > 1 else " = ", end='')
    fat = fat * num
    num -= 1

print(f"{fat}")
sair = input("ENTER para sair... ")