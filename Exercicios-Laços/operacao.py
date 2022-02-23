 
num1 = int(input("Digite o 1º valor: "))
num2 = int(input("Digite o 2º valor: "))
maior = num1
if num2 > maior:
    maior = num2
soma = 0
mult = 0
escolha = 0

while escolha != 5:
    print("-----------------------")
    print("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa""")
    escolha = int(input("Opção: "))
    if escolha > 5 or escolha < 1:
        print("Opção Inválida! Tente novamente..")
    elif escolha == 1:
        soma = num1 + num2
        print(f"SOMA --> {num1} + {num2} = {soma}")
    elif escolha == 2:
        mult = num1 * num2
        print(f"MULTIPLICAÇÃO --> {num1} x {num2} = {mult}")
    elif escolha == 3:
        print(f"O maior entre {num1} e {num2} é {maior}")
    elif escolha == 4:
        num1 = int(input("Digite o 1º valor: "))
        num2 = int(input("Digite o 2º valor: "))
        maior = num1
        if num2 > maior:
            maior = num2


print("\nFim do programa...\n")
sair = input("ENTER para sair... ")

