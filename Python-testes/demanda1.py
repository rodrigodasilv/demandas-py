# Faça um programa que solicite o nome do usuário e posteriormente mostre uma
# mensagem: Olá nomedousuário.

usuario=''
while not usuario.strip():
    usuario = input('Informe seu nome: ')
print ('Olá, ', usuario)