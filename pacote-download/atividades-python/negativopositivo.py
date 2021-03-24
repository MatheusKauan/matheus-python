#Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo
numero = int(input('Digite um numero: '))
print()
if numero < 0:
    print('O numero é negativo!!')

elif numero > 0:
    print('O numero é positivo!!')

else:
    print('O numero é zero')