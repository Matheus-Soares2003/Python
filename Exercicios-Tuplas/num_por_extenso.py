from time import sleep

num_extenso = ('zero','um','dois','três','quatro','cinco','seis',   'sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num_user = int(input("Digite um número entre 0 e 20: "))
    if num_user > 20 or num_user < 0:
        print('Numero inválido! Tente novamente...')
        sleep(1.5)
    else:
        break
print(f'Você digitou o número {num_extenso[num_user]}')
sair = input("ENTER para sair... ")

