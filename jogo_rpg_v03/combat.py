from time import sleep

cat_jump = ['k', 'K', 'p', 'P', 'r', 'R']

def warrior_combat(warrior_character, monster):
    print('==========Combat Start!!==========')
    print()
    sleep(0.5)
    while warrior_character.life > 0 and monster.life > 0:
        if warrior_character.luck > monster.luck:
            print(f'{warrior_character.name} has more luck, start the round!')
            character_choice = input('What do you want to do?'
                               '\nCombat: [c/C]'
                               '\nCheck Status: [s/S]'
                               '\nRun: [r/R]')
            if character_choice == 'c' or character_choice == 'C':
                sleep(0.5)
                print()
                warrior_character.melee_attack()
                character_damage = warrior_character.kick_attack()
                monster.life -= character_damage
                print(f'Monster HP: {monster.life}/{monster.max_life}'
                      f'\nDamage Taken: {character_damage}'
                      f'============'
                      f'\n')

