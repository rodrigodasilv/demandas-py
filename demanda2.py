# Faça um programa que calcule o IMC de uma pessoa, mostre o IMC e uma das
# mensagens abaixo de acordo com seu índice.
# Resultado | Mensagem
# Abaixo de 17 | Muito abaixo do peso
# Entre 17 e 18,49 | Abaixo do peso
# Entre 18,5 e 24,99 | Peso normal
# Entre 25 e 29,99 | Acima do peso
# Entre 30 e 34,99 | Obesidade I
# Entre 35 e 39,99 | Obesidade II (severa)
# Acima de 40 | Obesidade III (mórbida)

peso=''
altura=''

while peso==0 or not peso.strip() or altura==0 or not altura.strip():
    peso = input('Informe o seu peso: (EM KG) ')
    altura = input('Informe a sua altura: (EM M) ')

altura = float(altura)
peso = float(peso)
imc = peso / (altura*altura)
imc = round(imc, 2)

if imc<17:
    print('Seu IMC é de: ', imc , ' e você está muito abaixo do peso')
elif imc>=17 and imc<=18.49:
    print('Seu IMC é de: ' , imc , ' e você está abaixo do peso')
elif imc>=18.5 and imc<=24.99:
    print('Seu IMC é de: ' , imc , ' e você está com o peso normal')
elif imc>=25 and imc<=29.9:
    print('Seu IMC é de: ' , imc , ' e você está acima do peso')
elif imc>=30 and imc<=34.99:
    print('Seu IMC é de: ' , imc , ' e você está obeso')
elif imc>=35 and imc<=39.99:
    print('Seu IMC é de: ' , imc , ' e você está muito obeso')
elif imc>=40:
    print('Seu IMC é de: ' , imc , ' e você está extremamente obeso')
else:
    print('ERRO')
