sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

while sexo not in 'MmFf':    
    print("Opcão Inválida. Tente Novamente")
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

print(f"Sexo {sexo} registrado com sucesso!")
sair = input("ENTER para sair... ")