from random import randint

class human:
    def __init__(self, name):
        self.life = 10
        self.stre = 1
        self.intel = 1
        self.dex = 1
        self.luck = randint(0,3)
        self.level = 1
        self.xp = self.level * 20
        self.name = name


    def attribute_print(self):
        print(f'Life: {self.life}'
        f'\nStrenght: {self.stre}'
        f'\nIntelligence: {self.intel}'
        f'\nDexterity: {self.dex}'
        f'\nLuck: {self.luck}')
        print(f'' * 25)
        print(f'Level: {self.level}'
        f'\nXP: {self.xp}')

#lets say that stre, intel and dex are main stats, and life its essential but secondary
#sooo 1 point of essential stats = 2.5 more importance at general effect
#so 2 essential stats = 5 life (in weight)

    def warrior(self): # +3 stre, +1 intel, +2 dex, +5 life = 3+1+2 + "5 / 2.5" = 8
        self.life += 5
        self.stre += 3
        self.intel += 1
        self.dex += 2
        self.damage = self.stre * 1.5

    def archer(self): # +1 stre, +1 intel, +4 dex, +5 life = 1 + 1 + 4 + 2 = 8
        self.life += 5
        self.stre += 1
        self.intel += 1
        self.dex += 4
        self.damage = self.dex * 1.5

    def mage(self): # +0 stre, + 5 intel, + 1 dex, + 5 life = 0 + 5 + 1 + 2 = 8
        self.life += 5
        self.stre += 0
        self.intel += 5
        self.dex += 1
        self.damage = self.intel * 1.5

    def xp_gain(self, monster_xp):
        self.xp -= monster_xp

    def level_up(self):
        if self.xp <= 0:
            print('Level up!')



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

