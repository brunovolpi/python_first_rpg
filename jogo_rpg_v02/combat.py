

def combat(character, monster):
    print('========== Combat time! ==========')
    if character.job == 'warrior':
        while character.life > 0 and monster.life > 0:
            status = input('Combat: [c/C]'
                           '\nStatus: [s/S]')
            while status != 'c' and status != 'C' and status != 's' and status != 'S':
                if status == 'c' or status == 'C':
                    pass
                elif status == 's' or status == 'S':
                    print(f'===== Monster ====='
                          f'\nHP: {monster.life}'
                          f'\n===== Player ====='
                          f'\nHP: {character.life}')
                else:
                    status = input('Sorry, your typing did not matched the options, try again!')
                print()
            damage = character.skill_attack()
            monster.life -= damage
            print()
            print(f'===== Monster ====='
                  f'\nSkill damage: {damage}'
                  f'\nMonster HP: {monster.life}'
                  f'\n===================')
            if monster.life > 0:
                damage = monster.damage
                character.life -= damage
                print()
                print(f'===== Player ====='
                      f'\nMonster damage: {damage}'
                      f'\n{character.name} HP: {character.max_life} / {character.life}'
                      f'\n==================')
            else:
                print()
                print('The monster is now dead.')
                print(f'XP gained: {monster.xp}'
                      f'\nXP to Level Up: {character.xp}')
                character.xp -= monster.xp
                if character.xp <= 0:
                    character.level_up()
    elif character.job == 'mage':
        while character.life > 0 and monster.life > 0:
            status = input('Combat: [c/C]'
                           '\nStatus: [s/S]')
            if status == 'c' or status == 'C':
                pass
            elif status == 's' or status == 'S':
                print(f'===== Monster ====='
                      f'\nHP: {monster.life}'
                      f'\n===== Player ====='
                      f'\nHP: {character.life}')
            print()