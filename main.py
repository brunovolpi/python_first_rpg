from time import sleep
from rpg_construction import warrior
from rpg_construction import mage
from rpg_construction import archer
from rpg_construction import monster

def main():
    print('Hi and welcome to my game!'
          '\nThis is a pretty iniciant coder rpg game')
    print()
    name = input('So... tell me how do you wanna be called: ')

    #Character creation

    #Monster creation
    monster_noob = monster()
    monster.noob(monster_noob)

    monster_medium = monster()
    monster.medium(monster_medium)

    monster_advanced = monster()
    monster.advanced(monster_advanced)

    monster_boss = monster()
    monster.boss(monster_boss)


    job = input('You can choose a job:'
                           '\nMage (m/M)'
                           '\nArcher (a/A)'
                           '\nWarrior (w/W)')

    if job == 'm' or job == 'M':
        firstChar = mage(name)
        print('Congrats! You are a mage now!')
        print()
        firstChar.attribute_print()

    if job == 'a' or job == 'A':
        firstChar = archer(name)
        print('Congrats! You are an archer now!')
        print()
        firstChar.attribute_print()

    if job == 'w' or job == 'W':
        firstChar = warrior(name)
        print('Congrats! You are a warrior now!')
        print()
        firstChar.attribute_print()




                            ########## Combat definition ##########



    def combat_noob(character, monster):
        while firstChar.life > 0 and monster_noob.life > 0:
            print()
            monster_noob.life -= firstChar.attack(input('Choose your attack:'
                                                        '\nKick: [k/K]'
                                                        '\nPunch: [p/P]'
                                                        '\nRumble: [r/R]'
                                                        '\n'))
            print()
            print(f'\nHit: {firstChar.damage}'
                    f'Monster HP: {monster_noob.life}')
            if monster.life > 0:
                firstChar.life -= monster_noob.damage
                print(f'Taken: {monster_noob.damage}'
                        f'\nHP: {firstChar.life}')
            elif monster_noob.life <= 0:
                print('The monster is now dead...')
            else:
                print('You are dead!')

    def combat_noob(character, monster):
        while firstChar.life > 0 and monster_noob.life > 0:
            print()
            monster_noob.life -= firstChar.attack()
            print()
            print(f'\nHit: {firstChar.damage}'
                    f'\nMonster HP: {monster_noob.life}')
            if monster.life > 0:
                firstChar.life -= monster_noob.damage
                print(f'Taken: {monster_noob.damage}'
                        f'\nHP: {firstChar.life}')
            elif monster_noob.life <= 0:
                print('The monster is now dead...')
            else:
                print('You are dead!')


    #Introduction/Creation

    print('When your XP gets to 0, you will level up!')
    print('Now lets try a fight!')
    print()
    combat_noob(firstChar, monster_noob)
if '__name__' == '__main__':
    main()

main()