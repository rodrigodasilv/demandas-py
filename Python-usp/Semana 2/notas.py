# Exercício 2
# Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:
# Nota: 9/10
# Como trata-se de notas, vou usar o float!
primeiraNota = float(input('Digite a primeira nota: '))
segundaNota = float(input('Digite a segunda nota: '))
terceiraNota = float(input('Digite a terceira nota: '))
quartaNota = float(input('Digite a quarta nota: '))
notas = primeiraNota+ segundaNota+terceiraNota+quartaNota
media = notas/4
print('A média aritmética é: ', media)