# Exercício 5 - Verificando ordenação
# Receba 3 números inteiros na entrada e imprima crescente se eles forem dados em ordem crescente. Caso contrário, imprima não está em ordem crescente
# Nota:10/10

numero1 = int(input('Insira o primeiro número: '))
numero2 = int(input('Insira o segundo número: '))
numero3 = int(input('Insira o terceiro número: '))

if (numero1 < numero2 and numero2 < numero3):
    print('Crescente')
else:
    print('Não está em ordem crescente')