from time import sleep
from rpg_construction import human
from rpg_construction import monster
from combat import combat
from char_creation import character_creation

def main():

    #Game start!
    #Monsters
    monster_noob = monster()
    monster.noob(monster_noob)
    monster_medium = monster()
    monster.medium(monster_medium)
    monster_advanced = monster()
    monster.advanced(monster_advanced)
    monster_boss = monster()
    monster.boss(monster_boss)

    #Introduction/Creation
    print('Hi and welcome to my game!'
          '\nThis is a pretty iniciant coder rpg game')

    character_creation()

    print()
    print('When your XP gets to 0, you will level up!')
    print('Now lets try a fight!')
    print()
    combat(firstChar, monster_noob)


if '__name__' == '__main__':
    main()

main()