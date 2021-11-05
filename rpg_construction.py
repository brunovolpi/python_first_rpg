from random import randint
from weapons import basic_sword
#time to make one class for each job

def combat(character, monster):
    while character.life > 0 and monster.life > 0:
        print()
        monster.life -= character.attack() + monster.defense
        print()
        print(f'\nHit: {character.damage}'
              f'\nMonster HP: {monster.life}')
        if monster.life > 0:
            character.life -= monster.damage + character.defense
            print(f'Taken: {monster.damage}'
                  f'\nHP: {character.life}')
            if character.life <= 0:
                print('You are dead!')
                break
        elif monster.life <= 0:
            print('The monster is now dead...')
            pass
            character.xp -= monster.xp
            print(f'You gained: {monster.xp} XP')
            if character.xp <= 0:
                character.level_up()
                print()

class warrior:
    def __init__(self, name):
        self.job = 'warrior'
        self.stre = 4
        self.intel = 2
        self.dex = 2
        self.cons = 4
        self.defense = int(self.cons / 2)
        self.life = self.cons * 6
        self.luck = randint(0, 3)
        self.level = 1
        self.xp = self.level * 20
        self.name = name

    def level_up(self):
        print('Level up!')
        print()
        self.cons += 2
        self.stre += 3
        self.intel += 1
        self.dex += 1
        self.level += 1
        self.xp = self.level * 20


    def attack(self):
        self.damage = self.stre * 1.5
        punch = self.damage * 1.1
        kick = self.damage * 1.2
        rumble = self.damage * 1.5
        self.input = input('Kick: [k/K]'
                      '\nPunch: [p/P]'
                      '\nRumble: [r/R]')
        if self.input == 'p' or self.input == 'P':
            return int(punch)
        elif self.input == 'k' or self.input == 'K':
            return int(kick)
        elif self.input == 'r' or self.input == 'R':
            return int(rumble)

    def attribute_print(self):
        print(f'Life: {self.life}'
        f'\nStrenght: {self.stre}'
        f'\nIntelligence: {self.intel}'
        f'\nDexterity: {self.dex}'
        f'\nConstitution: {self.cons}'
        f'\nLuck: {self.luck}')
        print(f'' * 25)
        print(f'Level: {self.level}'
        f'\nXP Remainig: {self.xp}')


class archer:
    def __init__(self, name):
        self.job = 'archer'
        self.stre = 2
        self.intel = 2
        self.dex = 4
        self.cons = 3
        self.defense = int(self.cons / 2)
        self.life = self.cons * 5
        self.mana = self.intel * 3
        self.luck = randint(0, 3)
        self.level = 1
        self.xp = self.level * 20
        self.name = name


    def level_up(self):
        print('Level up!')
        self.cons += 1
        self.stre += 1
        self.intel += 1
        self.dex += 4
        self.level += 1
        self.xp = self.level * 20


    def attack(self):
        critical = randint(0, 100)
        self.damage = self.stre * 1.5
        self.pierce_damage = self.dex * 1.5
        punch = self.damage * 1.1
        kick = self.damage * 1.2
        stab = self.pierce_damage * 1.5
        self.input = input('Kick: [k/K]'
                           '\nPunch: [p/P]'
                           '\nStab: [s/S]')
        if self.input == 'p' or self.input == 'P':
            return int(punch)
        elif self.input == 'k' or self.input == 'K':
            return int(kick)
        elif self.input == 's' or self.input == 'S':
            if critical >= 90:
                return stab * 2
            else:
                return int(stab)

    def attribute_print(self):
        print(f'Life: {self.life}'
        f'\nMana: {self.mana}'
        f'\nStrenght: {self.stre}'
        f'\nIntelligence: {self.intel}'
        f'\nDexterity: {self.dex}'
        f'\nConstitution: {self.cons}'
        f'\nLuck: {self.luck}')
        print(f'' * 25)
        print(f'Level: {self.level}'
        f'\nXP Remainig: {self.xp}')

class mage:
    def __init__(self, name):
        self.job = 'mage'
        self.cons = 2
        self.defense = int(self.cons / 2)
        self.stre = 1
        self.intel = 5
        self.dex = 2
        self.luck = randint(0, 3)
        self.life = self.cons * 5
        self.mana = self.intel * 6
        self.level = 1
        self.xp = self.level * 20
        self.name = name

    def level_up(self):
        print('Level Up!')
        self.cons += 1
        self.stre += 1
        self.intel += 4
        self.dex += 1
        self.xp = self.level * 20
        self.level += 1

    def attack(self):
        self.damage = self.stre * 1.5
        self.magic_damage = self.intel * 1.5
        punch = self.damage * 1.1
        kick = self.damage * 1.2
        burn = self.magic_damage * 1.5
        freeze = self.magic_damage * 1.5
        self.input = input('Kick: [k/K]'
                           '\nPunch: [p/P]'
                           '\nBurn: [b/B]'
                           '\nFreeze: [f/F]')
        if self.input == 'p' or self.input == 'P':
            return int(punch)
        elif self.input == 'k' or self.input == 'K':
            return int(kick)
        elif self.input == 'b' or self.input == 'B':
            self.mana -= 5
            return int(burn)
        elif self.input == 'f' or self.input == 'F':
            self.mana -= 5
            return int(freeze)


    def attribute_print(self):
        print(f'Life: {self.life}'
              f'\nMana: {self.mana}'
              f'\nStrenght: {self.stre}'
              f'\nIntelligence: {self.intel}'
              f'\nDexterity: {self.dex}'
              f'\nConstitution: {self.cons}'
              f'\nLuck: {self.luck}')
        print(f'' * 25)
        print(f'Level: {self.level}'
              f'\nXP Remaining: {self.xp}')

class monster_noob:
    def __init__(self):
        self.life = 15
        self.damage = 3
        self.defense = 1
        self.xp = self.life * 2

class monster_medium:
    def __init__(self):
        self.life = 30
        self.damage = 7
        self.defense = 3
        self.xp = self.life * 2

class monster_high:
    def __init__(self):
        bonus_xp = randint(0, 100)
        self.life = 50
        self.damage = 12
        self.defense = 7
        self.xp = self.life * 2
        if bonus_xp >= 90:
            self.xp *= 1.2

class monster_boss:
    def __init__(self):
        bonus_xp = randint(0, 100)
        self.life = 200
        self.damage = 35
        self.defense = 15
        self.xp = self.life * 2
        if bonus_xp >= 90:
            self.xp *= 1.2
