# Exercício 1
# Escreva um programa que receba um número natural n n n na entrada e imprima n! n! n! (fatorial) na saída.
# Nota: 10/10

resultado = 1
n = int(input('Digite o valor de n: '))
while n>0:
    resultado = resultado * n
    n = n-1
print(resultado)
