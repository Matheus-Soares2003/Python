from random import randint

cont = 1
pc = randint(0,10)
print("Acabei de pensar em um número entre 0 e 10.")
jogador = int(input("Em que número eu pensei: "))

while jogador != pc:
    if jogador > pc:
        print("Menos... Tente mais uma vez.")
    elif jogador < pc:
        print("Mais... Tente mais uma vez.")
    cont += 1
    jogador = int(input("Em que número eu pensei: "))

print(f"Acertou com {cont} tentativas. Parabéns!")
sair = input("ENTER para sair... ")

    
