from time import sleep

cat_jump = ['k', 'K', 'p', 'P', 'r', 'R', 'c', 'C', 's', 'S']

def warrior_combat(warrior_character, monster):
    print('==========Combat Start!!==========')
    print()
    sleep(0.5)
    while warrior_character.life > 0 and monster.life > 0:
        if warrior_character.luck >= monster.luck:
            print(f'{warrior_character.name} has more luck, start the round!')
            character_choice = input('What do you want to do?'
                               '\nCombat: [c/C]'
                               '\nCheck Status: [s/S]'
                               '\nRun (like a chicken): [r/R]')
            while character_choice not in cat_jump:
                character_choice = input('\nInvalid option'
                                    '\nCombat: [c/C]'
                                    '\nCheck Status: [s/S]'
                                    '\nRun (like a chicken): [r/R]')
                if character_choice in cat_jump:
                    pass
            if character_choice == 'c' or character_choice == 'C':
                sleep(0.5)
                print()
                character_damage = warrior_character.melee_attack() - monster.defence
                monster.life -= character_damage
                print(f'Monster HP: {monster.life}/{monster.max_life}'
                      f'\nDamage Taken: {character_damage}'
                      f'============'
                      f'\n')
                if monster.life > 0:
                    sleep(0.5)
                    print()
                    monster_damage = monster.damage - warrior_character.defence
                    warrior_character.life -= monster_damage
                    print(f'{warrior_character.name} HP: {warrior_character.life}/{warrior_character.max_life}'
                          f'\nDamage Taken: {monster_damage}'
                          f'============'
                          f'\n')
                else:
                    print('You killed the monster.')
                    print(f'XP: {monster.xp}')
                    warrior_character.xp -= monster.xp
                    if warrior_character.xp <= 0:
                        warrior_character.level_up()
        else:
            print()
            print('The monster has more luck!')
            sleep(0.5)
            print()
            monster_damage = monster.damage - warrior_character.defence
            warrior_character.life -= monster_damage
            print(f'{warrior_character.name} HP: {warrior_character.life}/{warrior_character.max_life}'
                  f'\nDamage Taken: {monster_damage}'
                  f'============'
                  f'\n')
            if warrior_character.life > 0:
                character_choice = input('What do you want to do?'
                                         '\nCombat: [c/C]'
                                         '\nCheck Status: [s/S]'
                                         '\nRun (like a chicken): [r/R]')
                while character_choice not in cat_jump:
                    character_choice = input('\nInvalid option'
                                             '\nCombat: [c/C]'
                                             '\nCheck Status: [s/S]'
                                             '\nRun (like a chicken): [r/R]')
                    if character_choice in cat_jump:
                        pass
                if character_choice == 'c' or character_choice == 'C':
                    sleep(0.5)
                    print()
                    character_damage = warrior_character.melee_attack() - monster.defence
                    monster.life -= character_damage
                    print(f'Monster HP: {monster.life}/{monster.max_life}'
                          f'\nDamage Taken: {character_damage}'
                          f'============'
                          f'\n')
            if monster.life <= 0:
                print('You killed the monster.')
                print(f'XP: {monster.xp}')
                warrior_character.xp -= monster.xp
                if warrior_character.xp <= 0:
                    warrior_character.level_up()
                else:
                    pass

