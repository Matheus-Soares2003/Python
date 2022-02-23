def voto(ano):
    from datetime import date
    
    idade = date.today().year - ano
    if idade >= 18 and idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade < 16:
        return f"Com {idade} anos:NÃO VOTA"
    elif 16 <= idade > 18 or idade > 65:
        return f"Com {idade} anosVOTO OPCIONAL"
    

print("-" * 30)
nasc = int(input("Ano de Nascimento: "))
print(voto(nasc))

