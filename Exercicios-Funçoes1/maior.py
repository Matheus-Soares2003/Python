from time import sleep

def maior(*num):
    print("Analisando valores passados...")
    mai = 0
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if valor > mai:
            mai = valor
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}')
    print('-=' * 35)
    
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()