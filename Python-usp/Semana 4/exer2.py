# Exercício 2
# Receba um número inteiro positivo na entrada e imprima os n n n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
# Nota:10/10

impares=1
numero = int(input('Digite o valor de n: '))
while numero>0:
    print(impares)
    impares=impares+2
    numero=numero-1