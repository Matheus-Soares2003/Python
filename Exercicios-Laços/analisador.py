soma = 0
contF = 0
media = 0
maior = 0
pessoa = ''
for c in range(0, 4):
    print(f"-----{c + 1}ª PESSOA-----")
    nome = str(input("Nome: ")).title().strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    if sexo == "M" and idade > maior:
        maior = idade
        pessoa = nome
    if sexo == "F" and idade < 20:
        contF += 1
    soma += idade

media = soma / 4
print(f"A média de idade do grupo é de {media:.1f} anos")
print(f"O homem mais velho tem {maior} anos e se chama {pessoa}")
print(f"Ao todo são {contF} mulheres com menos de 20 anos")
sair = input("ENTER para sair... ")
