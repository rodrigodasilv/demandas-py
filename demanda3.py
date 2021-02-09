# A prefeitura de Pedra Lisa decidiu implantar um sistema de rodízio de veículos, e
# lhe solicitou um algoritmo em que o usuário informe o último número da placa de seu
# carro, para que o programa possa informar que dia da semana esse carro não pode ir
# às ruas, seguindo a tabela abaixo:

# Dia da semana Placas que não podem circular
# Segunda-feira 0 e 5
# Terça-feira 1 e 6
# Quarta-feira 2 e 7
# Quinta-feira 3 e 8
# Sexta-feira 4 e 9

placa=''

while not placa.strip() or not placa.isnumeric():
    placa = input('Informe o último número da placa do seu carro: ')

placa = float(placa)

if placa>9 or placa<0:
    print('ERRO')
elif placa==0 or placa==5:
    print('Esse carro não pode ir às ruas nas segundas feiras!')
elif placa==1 or placa==6:
    print('Esse carro não pode ir às ruas nas terças feiras!')
elif placa==2 or placa==7:
    print('Esse carro não pode ir às ruas nas quartas feiras!')
elif placa==3 or placa==8:
    print('Esse carro não pode ir às ruas nas quintas feiras!')
elif placa==4 or placa==9:
    print('Esse carro não pode ir às ruas nas sextas feiras!')