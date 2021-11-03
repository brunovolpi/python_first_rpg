from time import sleep
from rpg_construction import human
from rpg_construction import monster
from combat import combat
from char_creation import character_creation

def main():
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
    def combat_noob(human, monster):
        while firstChar.life > 0 or monster.life > 0:
            monster.life - human.damage
            print(f'Hit: {firstChar.damage}'
                  f'\nMonster HP: {monster.life}')
            if monster.life > 0:
                damage_taken = human.life - monster.damage
                human.life - monster.damage
                print(f'Taken: {damage_taken}'
                      f'\nHP: {human.life}')

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