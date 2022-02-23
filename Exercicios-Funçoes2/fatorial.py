def fatorial(num, show=False):
    """
    => Calcula o fatorial de um numero
    : num -> Numero a ser calculado
    : show -> (opcional) Mostrar ou nao a conta
    : return -> retorna o valor do fatorial de num
    """
    print('-' * 30)
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    if show==True:
        for c in range(num, 0, -1):
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')    
    return f

print(fatorial(7, show=True))
