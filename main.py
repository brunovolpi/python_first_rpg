from time import sleep
from rpg_construction import human
from rpg_construction import monster

def main():
    print('Hi and welcome to my game!'
          '\nThis is a pretty iniciant coder rpg game')
    print()
    name = input('So... tell me how do you wanna be called: ')

    #Character creation
    firstChar = human(name)

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
        human.mage(firstChar)
        print('Congrats! You are a mage now!')
        firstChar.attribute_print()

    if job == 'a' or job == 'A':
        human.archer(firstChar)
        print('Congrats! You are an archer now!')
        print()
        firstChar.attribute_print()

    if job == 'w' or job == 'W':
        human.warrior(firstChar)
        print('Congrats! You are a warrior now!')
        firstChar.attribute_print()

    def combat(human, monster):
        if firstChar == human.warrior:
            while firstChar.life > 0 and monster_noob.life > 0:
                firstChar.warrior_attacks()

        # Combat definition
    def combat(human, monster):
        while firstChar.life > 0 and monster_noob.life > 0:
            monster_noob.life -= firstChar.damage
            print(f'Hit: {firstChar.damage}'
                    f'\nMonster HP: {monster_noob.life}')
            if monster.life > 0:
                firstChar.life -= monster_noob.damage
                print(f'Taken: {monster_noob.damage}'
                        f'\nHP: {firstChar.life}')
            else:
                print('The monster is now dead.')

    #Introduction/Creation

    print('When your XP gets to 0, you will level up!')
    print('Now lets try a fight!')
    print()
    combat(firstChar, monster_noob)
if '__name__' == '__main__':
    main()

main()