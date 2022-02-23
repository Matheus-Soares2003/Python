from datetime import datetime
pessoa = {}
pessoa['Nome'] = str(input("Nome: "))
ano_Nasc = int(input("Ano de Nascimento: "))
pessoa['Idade'] = datetime.now().year - ano_Nasc
pessoa['CTPS'] = int(input("Carteira de Trabalho (0 não tem): "))
if pessoa['CTPS'] > 0:
    pessoa["Contratação"] = int(input("Ano de Contratação: "))
    pessoa['Salário'] = float(input("Salário: R$ "))
    pessoa['Aposentadoria'] = (pessoa["Contratação"] + 35) - ano_Nasc
    
print("-=" * 35)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
