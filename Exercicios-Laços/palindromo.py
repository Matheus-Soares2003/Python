frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f"{junto} de trás pra frente vira {inverso}")
if inverso == junto:
    print("Temos um palindormo!")
else:
    print("A frase digitada não é um palindromo!")
sair = input("ENTER para sair... ")