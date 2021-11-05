from time import sleep

from rpg_construction import warrior
from rpg_construction import mage
from rpg_construction import archer

from rpg_construction import monster_noob
from rpg_construction import monster_medium
from rpg_construction import monster_high
from rpg_construction import monster_boss


def main():
    print('Hi and welcome to my game!'
          '\nThis is a pretty iniciant coder rpg game')
    print()
    name = input('So... tell me how do you wanna be called: ')

    #Character creation

    #Monster creation
    beginner_monster = monster_noob()
    intermediate_monster = monster_medium()
    higher_monster = monster_high()
    boss = monster_boss()


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

    def combat(character, monster):
        while character.life > 0 and monster.life > 0:
            print()
            monster.life -= character.attack() + monster.defense
            print()
            print(f'\nHit: {character.damage}'
                    f'\nMonster HP: {monster.life}')
            if monster.life > 0:
                character.life -= monster.damage
                print(f'Taken: {monster.damage}'
                        f'\nHP: {character.life}')
                if character.life <= 0:
                    print('You are dead!')
                    break
            elif monster.life <= 0:
                print('The monster is now dead...')


    print('When your XP gets to 0, you will level up!')
    print('Now lets try a fight!')
    print()
    combat(firstChar, boss)
    firstChar.attribute_print()
if '__name__' == '__main__':
    main()

main()