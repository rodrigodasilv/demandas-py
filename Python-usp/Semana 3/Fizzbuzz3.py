# Exercícios 4 - FizzBuzz parcial, parte 3
# Receba um número inteiro na entrada e imprima FizzBuzz na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
# Nota: 10/10

numero = int(input('Insira um número inteiro: '))
if (numero%5==0 and numero%3==0):
    print ('FizzBuzz')
else:
    print (numero)