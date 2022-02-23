num = (int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")))

print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro valor 3 apareceu na posição {num.index(3) + 1}')
else:
    print("O valor 3 não foi digitado.")
print('Os valores pares digitados foram ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
print()
sair = input("ENTER para sair... ")
