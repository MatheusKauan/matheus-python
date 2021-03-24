ano = int(input('Qual o ano que vc nasceu?'))#pergunta ao usuario o ano nascido
print(ano)
idade = 2021 - ano # faz a subtração do ano atual com o ano nascido

print()#pula linha

if idade >= 18 and idade == 79 :
    print('Você é adulto tem', idade, 'anos!')

elif idade < 0:
    print('Não existe idade negativa')

elif idade > 120:
    print('Idade invalida')

elif idade >= 80:
    print('O senhor ja é bem idoso tem',idade,'anos')

else:
    print('Você não é adulto tem', idade, 'anos')