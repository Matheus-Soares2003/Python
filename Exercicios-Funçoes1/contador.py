from time import sleep

def contador(i, f, r):
    """
    ->Faz uma contagem e mostra na tela.
    :i -> Inicio da contagem
    :f -> Fim da contagem
    :r -> Razao / Passo da contagem
    :return -> Sem retorno
    """
    print("-=" * 20)
    if r < 0:
        r = r * -1
    if r == 0:
        r = 1
    print(f"Contagem de {i} até {f} de {r} em {r}")
    if i <= f:
        for c in range(i, (f + 1), r):
            print(f'{c} ', end='', flush=True)
            sleep(0.5)      
    else:
        for c in range(i, (f - 1), -r):
            print(f'{c} ', end='', flush=True)
            sleep(0.5)       
    print("FIM!")    

contador(1, 10, 1)
contador(10, 0, 2)
print("-=" * 20)
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Ínicio: "))
fim = int(input("Fim: "))
razao = int(input("Passo: "))
contador(inicio, fim, razao)

