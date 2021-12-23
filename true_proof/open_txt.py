variavel_aleatoria = open('criar_texto.txt', 'w')
variavel_aleatoria.write('o davi já quer desistir')
variavel_aleatoria.close()

variavel_aleatoria = open('criar_texto.txt', 'r')
print(variavel_aleatoria.read())