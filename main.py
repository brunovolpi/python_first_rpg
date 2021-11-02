from time import sleep
from rpg_construction import human
from rpg_construction import monster

def main():

    #Game start!
    print('Hi and welcome to my game!'
          '\nThis is a pretty iniciant coder rpg game'
          '\n')
    name = input('So express how you want to be called: ')
    print()
    print(f'Okay {name}, pleased to meet you!')
    firstChar = human(name)
    print()
    print('In this game default attributes are:'
          '\nLife: 10'
          '\nStrength: 1'
          '\nIntelligence: 1'
          '\nDexterity: 1'
          '\nLuck: random from 0 to 1')
    print('-' * 30)
    sleep(3)

    print('In this game there are 3 main classes: Warrior, Archer and Mage.'
          '\nEach class boosts attributes in a unique way'
          '\nWarriors get more HP when level up, such as Archers get more Dex and Mages get Int')
    job = input('Choose your destiny: Warrior (w/W)'
                '\nArcher (a/A)'
                '\nMage (m/M)'
                '\nPress the correspondent key to select a class: ')
    print()
    if job == 'w' or job == 'W':
        human.warrior(firstChar)
        print('Okay, you are a warrior now'
              '\nEnjoy your starting attributes!')
        firstChar.attribute_print()

    if job == 'a' or job == 'A':
        human.archer(firstChar)
        print('Okay, you are an archer now'
              '\nEnjoy your starting attributes!')
        firstChar.attribute_print()

    if job == 'm' or job == 'M':
        human.mage(firstChar)
        print('Okay, you are a mage now'
              '\nEnjoy your starting attributes!')
        firstChar.attribute_print()


if '__name__' == '__main__':
    main()

main()