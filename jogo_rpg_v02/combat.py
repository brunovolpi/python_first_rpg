

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
                          f'\nHP: {monster.life}/{monster.max_life}'
                          f'\n===== Player ====='
                          f'\nHP: {character.life}')
                else:
                    status = input('Sorry, your typing did not matched the options, try again!'
                                   '\nCombat: [c/C]'
                                   '\nStatus: [s/S]')
                print()
            damage = character.skill_attack()
            monster.life -= damage
            print()
            print(f'===== Monster ====='
                  f'\nSkill damage: {damage}'
                  f'\nMonster HP: {monster.life}/{monster.max_life}'
                  f'\n===================')
            if monster.life > 0:
                damage = monster.damage
                character.life -= damage
                print()
                print(f'===== Player ====='
                      f'\nMonster damage: {damage}'
                      f'\n{character.name} HP: {character.life}/{character.max_life}'
                      f'\n==================')
            else:
                print()
                print('The monster is now dead.')
                print(f'XP gained: {monster.xp}'
                      f'\nXP to Level Up: {character.xp}')
                character.xp -= monster.xp
                if character.xp <= 0:
                    character.level_up()
    elif character.job == 'mage': #I really need to create some functions for 'battle_choice' or something
        while character.life > 0 and monster.life > 0:
            status = input('Combat: [c/C]'
                           '\nStatus: [s/S]')
            if status == 'c' or status == 'C':
                combat_type = input('Chaos Magic: [cm/CM]'
                                    '\nHarmonic Magic: [hm/HM]')
                while combat_type != 'cm' and combat_type != 'CM' and combat_type != 'hm' and combat_type != 'HM':
                    combat_type = input('Sorry, no valid option typed, try again!'
                                        '\nChaos Magic: [cm/CM]'
                                        '\nHarmonic Magic: [hm/HM]')
                    if combat_type == 'cm' or combat_type == 'CM':
                        damage = character.chaos_magic()
                        monster.life -= damage
                        print(f'===== Monster ====='
                        f'\nSkill damage: {damage}'
                        f'\nMonster HP: {monster.life}/{monster.max_life}'
                        f'\n===================')
                    elif combat_type == 'hm' or combat_type == 'HM':
                        heal = character.harmonic_magic()
                        character.life += heal
                        if character.life > character.max_life:
                            diff = character.life - character.max_life
                            character.life -= diff
                        else:
                            pass
                if combat_type == 'cm' or combat_type == 'CM':
                    damage = character.chaos_magic()
                    monster.life -= damage
                    print(f'===== Monster ====='
                          f'\nSkill damage: {damage}'
                          f'\nMonster HP: {monster.life}/{monster.max_life}'
                          f'\n===================')
                elif combat_type == 'hm' or combat_type == 'HM':
                    heal = character.harmonic_magic()
                    character.life += heal
                    if character.life > character.max_life:
                        diff = character.life - character.max_life
                        character.life -= diff
                    else:
                        pass
                    print(f'\n===== Player ====='
                          f'\nHeal: {heal}'
                          f'\nHP: {character.life}/{character.max_life}')
            elif status == 's' or status == 'S':
                print(f'===== Monster ====='
                      f'\nHP: {monster.life}'
                      f'\n===== Player ====='
                      f'\nHP: {character.life}')
            if monster.life > 0:
                damage = monster.damage
                character.life -= damage
                print()
                print(f'===== Player ====='
                      f'\nMonster damage: {damage}'
                      f'\n{character.name} HP: {character.life}/{character.max_life}'
                      f'\n==================')
            else:
                print('The monster is now dead...')
                character.xp -= monster.xp
                if character.xp <= 0:
                    character.level_up()
            print()