print("\nGerador de PA")
print("-=" * 10)

a1 = int(input("Primeiro termo: "))
R = int(input("Razão da PA: "))
a10 = a1 + 9 * R
c = a1
while c <= a10:
    print(f"{c}", end='')
    print(" -> " if c < a10 else " -> FIM ", end='')
    c = c + R
print("\n")
sair = input("ENTER para sair... ")
