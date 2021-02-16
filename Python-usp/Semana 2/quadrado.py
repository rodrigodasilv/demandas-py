# Exercício 1
# Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.
# Observação: a saída deve estar no formato: "perímetro: x - área: y"
# Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez
# Nota: 8/10

lado = int(input('Digite o valor correspondente ao lado de um quadrado: '))
area = lado ** 2
perimetro = lado * 4
print ('Perímetro: ', perimetro,'- Área: ', area)