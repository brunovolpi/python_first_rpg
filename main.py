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

    #Combat definition
    def combat(human, monster):
        while firstChar.life > 0 or monster.life > 0:
            monster.life - firstChar.damage
            print(f'Hit: {firstChar.damage}'
                  f'\nMonster HP: {monster.life}')
            if monster.life > 0:
                firstChar.life - monster.damage
                print(f'Taken: {monster.damage}'
                      f'\nHP: {firstChar.life}')

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

    if job == 'g' or job == 'G':
        human.warrior(firstChar)
        print('Congrats! You are a warrior now!')
        firstChar.attribute_print()

    #Introduction/Creation

    print('When your XP gets to 0, you will level up!')
    print('Now lets try a fight!')
    print()

if '__name__' == '__main__':
    main()

main()