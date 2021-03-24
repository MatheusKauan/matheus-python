#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.


salario = float(input('Qual o seu salario? '))

if salario < 280.00:
    aumento = salario * 0.2
    salario_aumentado = salario + aumento
    print('Salario antes do aumento é de: R$',salario)

    print()
    print('O percentual aplicado foi de 20%')

    print()
    print('O valor do aumento é de: R${:.2f} '.format(aumento))

    print()
    print('O novo salario é: R$',salario_aumentado)


elif salario >= 280.00 and salario < 699.99:
    aumento = salario * 0.15
    salario_aumentado = salario + aumento
    print('Salario antes do aumento é de: R$',salario)
    
    print()
    print('O percentual aplicado foi de 15%')
    
    print()
    print('O valor do aumento é de: R${:.2f}'.format(aumento))
    
    print()
    print('O novo salario é: R$', salario_aumentado)

elif salario >=700.00 and salario <1500.00:
    aumento = salario * 0.10
    salario_aumentado = salario + aumento
    print('Salario antes do aumento é de: R$',salario)
    
    print()
    print('O percentual aplicado foi de 10%')
    
    print()
    print('O valor do aumento é de: R${:.2f}'.format(aumento))
    
    print()
    print('O novo salario é: R$', salario_aumentado)

else:
    aumento = salario * 0.05
    salario_aumentado = salario + aumento
    print('Salario antes do aumento é de: R$',salario)
    
    print()
    print('O percentual aplicado foi de 5%')
    
    print()
    print('O valor do aumento é de: R${:.2f}'.format(aumento))
    
    print()
    print('O novo salario é: R$', salario_aumentado)

