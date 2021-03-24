numero = int(input('Digite um numero'))
fatorial = numero
contador = 1

while (numero - contador) > 1:
    fatorial = fatorial * (numero-contador)
    contador +=1
print('O fatorial de ', numero,'é', fatorial)