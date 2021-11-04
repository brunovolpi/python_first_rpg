from random import randint

#time to make one class for each job

class warrior:
    def __init__(self, name):
        self.life = 15
        self.stre = 4
        self.intel = 2
        self.dex = 2
        self.luck = randint(0, 3)
        self.level = 1
        self.xp = self.level * 20
        self.name = name

    def level_up(self):
        if self.xp <= 0:
            self.life += 6
            self.stre += 3
            self.intel += 0
            self.dex += 1
        else:
            return False

    def attack(self, input):
        self.damage = self.stre * 1.5
        punch = self.damage * 1.1
        kick = self.damage * 1.1
        rumble = (self.damage * 1.5)
        if input == 'p' or input == 'P':
            return punch
        elif input == 'k' or input == 'K':
            return kick
        elif input == 'r' or input == 'R':
            return rumble

    def attribute_print(self):
        print(f'Life: {self.life}'
        f'\nStrenght: {self.stre}'
        f'\nIntelligence: {self.intel}'
        f'\nDexterity: {self.dex}'
        f'\nLuck: {self.luck}')
        print(f'' * 25)
        print(f'Level: {self.level}'
        f'\nXP: {self.xp}')


class archer:
    def __init__(self, name):
        self.life = 12
        self.stre = 2
        self.intel = 2
        self.dex = 4
        self.luck = randint(0, 3)
        self.level = 1
        self.xp = self.level * 20
        self.name = name

    def level_up(self):
        if self.xp <= 0:
            self.life += 3
            self.stre += 1
            self.intel += 1
            self.dex += 5
        else:
            return False

    def attribute_print(self):
        print(f'Life: {self.life}'
        f'\nStrenght: {self.stre}'
        f'\nIntelligence: {self.intel}'
        f'\nDexterity: {self.dex}'
        f'\nLuck: {self.luck}')
        print(f'' * 25)
        print(f'Level: {self.level}'
        f'\nXP: {self.xp}')

class mage:
    def __init__(self, name):
        self.life = 10
        self.stre = 1
        self.intel = 5
        self.dex = 2
        self.luck = randint(0, 3)
        self.level = 1
        self.xp = self.level * 20
        self.name = name

    def level_up(self):
        if self.xp <= 0:
            self.life += 2
            self.stre += 0
            self.intel += 7
            self.dex += 1
        else:
            return False

    def attribute_print(self):
        print(f'Life: {self.life}'
        f'\nStrenght: {self.stre}'
        f'\nIntelligence: {self.intel}'
        f'\nDexterity: {self.dex}'
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

