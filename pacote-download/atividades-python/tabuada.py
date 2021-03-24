#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada.

numero = int(input('Digite um numero'))
contador = 1
soma = 0
while contador <11:
    soma = numero * contador 
    print('A multiplicação de {0} X {1} = {2}'.format(numero,contador,soma))
    contador += 1
   
