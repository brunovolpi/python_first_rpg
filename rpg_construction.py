from random import randint

#time to make one class for each job

class warrior:
    def __init__(self, name):
        self.stre = 4
        self.intel = 2
        self.dex = 2
        self.cons = 4
        self.life = self.cons * 6
        self.luck = randint(0, 3)
        self.level = 1
        self.xp = self.level * 20
        self.name = name

    def level_up(self):
        if self.xp <= 0:
            self.cons += 2
            self.stre += 3
            self.intel += 1
            self.dex += 1
        else:
            return False


    """def monster_fight(self):
        while firstChar.life > 0 and monster_noob.life > 0:
            print()
            monster_noob.life -= firstChar.attack()
            print()
            print(f'\nHit: {firstChar.damage}'
                    f'Monster HP: {monster_noob.life}')
            if monster.life > 0:
                firstChar.life -= monster_noob.damage
                print(f'Taken: {monster_noob.damage}'
                        f'\nHP: {firstChar.life}')
            elif monster_noob.life <= 0:
                print('The monster is now dead...')"""

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
        f'\nXP: {self.xp}')


class archer:
    def __init__(self, name):
        self.stre = 2
        self.intel = 2
        self.dex = 4
        self.cons = 3
        self.life = self.cons * 5
        self.mana = self.intel * 3
        self.luck = randint(0, 3)
        self.level = 1
        self.xp = self.level * 20
        self.name = name

    def level_up(self):
        if self.xp <= 0:
            self.cons += 1
            self.stre += 1
            self.intel += 1
            self.dex += 4
        else:
            return False




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
        f'\nXP: {self.xp}')

class mage:
    def __init__(self, name):
        self.cons = 2
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
        if self.xp <= 0:
            self.cons += 1
            self.stre += 1
            self.intel += 4
            self.dex += 1
        else:
            return False

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
              f'\nXP: {self.xp}')

class monster:
    def __init__(self):
        self.life = 0
        self.damage = 0
        self.defense = 0
        xp = self.life * 1.5

    def noob(self):
        self.life += 10
        self.damage += 3
        self.defense += 1

    def medium(self):
        self.life += 25
        self.damage += 8
        self.defense += 4

    def advanced(self):
        self.life += 60
        self.damage += 20
        self.defense += 10

    def boss(self):
        self.life += 150
        self.damage += 50
        self.defense += 30

