# Exercício 3 - Vogais
# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
# Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.
# Nota:10/10

def vogal(a):
    a = a.lower()
    if (a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
        return True
    else:
        return False