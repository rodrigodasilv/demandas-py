# Exercícios 3 - FizzBuzz parcial, parte 2 
# Receba um número inteiro na entrada e imprima Buzz se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
# Nota: 10/10

numero = int(input('Insira um número inteiro: '))
if (numero%5==0):
    print ('Buzz')
else:
    print (numero)