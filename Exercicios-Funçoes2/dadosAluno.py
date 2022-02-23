def notas(*num, sit=False):
    s = {}
    s['total'] = len(num)
    s['maior'] = max(num)
    s['menor'] = min(num)
    s['media'] = sum(num) / len(num)
    if sit==True:
        if s['media'] < 6:
            s['situação'] = 'RUIM'
        elif 6 < s['media'] < 7:
            s['situação'] = 'RAZOÁVEL'
        else:
            s['situação'] = 'BOA'
    return s
        
#Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
