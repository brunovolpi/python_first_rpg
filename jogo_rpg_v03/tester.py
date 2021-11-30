cat_jump = ['k', 'K', 'p', 'P', 'r', 'R']
character_input = input('bota qq coisa aí')


for i in cat_jump:
    if character_input != i:
        print('entrou')
        break
    else:
        print('saiu')
