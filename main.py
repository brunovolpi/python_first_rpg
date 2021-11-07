from time import sleep
from rpg_construction import combat


from rpg_construction import warrior
from rpg_construction import mage
from rpg_construction import archer

from rpg_construction import monster_noob
from rpg_construction import monster_medium
from rpg_construction import monster_high
from rpg_construction import monster_boss

from weapons import basic_sword
from weapons import basic_bow
from weapons import basic_shield
from weapons import basic_wand


def main():

    print('Hi and welcome to my game!'
          '\nThis is a pretty iniciant coder rpg game')
    print()
    sleep(0.5)
    name = input('So... tell me how do you wanna be called: ')
    print()
    sleep(0.5)
    print(f'Pleased to meet you {name}, lets begin our game!')
    print()
    sleep(0.5)

    #Monster creation
    beginner_monster = monster_noob()
    intermediate_monster = monster_medium()
    higher_monster = monster_high()
    boss = monster_boss()

    print('There are 3 jobs:'
          '\nWarrior: High HP, strong melee tanks'
          '\nArchers: Critical chance attacks, hibrid gameplay'
          '\nMages: Very strong spells, low HP')
    print()
    job = input('Choose a job:'
                           '\nWarrior (w/W)'
                           '\nArcher (a/A)'
                           '\nMage (m/M)')

    while job != 'w' and job != 'W' and job != 'a' and job != 'A' and job != 'm' and job != 'M':
        job = input('\nTry the matching options again'
                    '\n'
                    '\nChoose a job:'
                    '\nWarrior (w/W)'
                    '\nArcher (a/A)'
                    '\nMage (m/M)')

        if job == 'm' or job == 'M':
            firstChar = mage(name)
            print('Congrats! You are a mage now!')
            print()
            firstChar.attribute_print()
            sleep(0.5)
            pass

        elif job == 'a' or job == 'A':
            firstChar = archer(name)
            print('Congrats! You are an archer now!')
            print()
            firstChar.attribute_print()
            sleep(0.5)
            pass

        elif job == 'w' or job == 'W':
            firstChar = warrior(name)
            print('Congrats! You are a warrior now!')
            print()
            firstChar.attribute_print()
            sleep(0.5)
            pass

    print('When your XP gets to 0, you will level up!')
    print('Now lets try a fight!')
    print()
    sleep(0.5)
    combat(firstChar, beginner_monster)
    firstChar.attribute_print()
    print()
    print('Now lets equip you something!')
    if firstChar.job == 'warrior':
        basic_sword(firstChar)
        basic_shield(firstChar)
    elif firstChar.job == 'archer':
        basic_bow(firstChar)
    elif firstChar.job == 'mage':
        basic_wand(firstChar)
    firstChar.attribute_print()
if '__name__' == '__main__':
    main()

main()