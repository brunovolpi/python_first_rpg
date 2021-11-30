#I can try to randomize the monster that will appear by creating minimun - maximun stats
from random import randint

def combat_difficult(grade_level):
    difficult = randint(0, 100)
    if grade_level == 'noob':
        if difficult <= 50:
            monster = noob()
            monster.easy()
            print('An easy monster!')
            return monster
        elif 51 <= difficult <= 80:
            monster = noob()
            monster.medium()
            print('A medium monster!')
            return monster
        else:
            monster = noob()
            monster.hard()
            print(type(monster))
            print('A hard monster!')
            return monster
    elif grade_level == 'medium':
        if difficult <= 50:
            monster = medium()
            monster.easy()
            print('An easy monster!')
            return monster
        elif 51 <= difficult <= 80:
            monster = medium()
            monster.medium()
            print('A medium monster!')
            return monster
        else:
            monster = medium()
            monster.hard()
            print('A hard monster!')
            return monster



class noob:
    def __init__(self):
        self.stre = 1
        self.dex = 1
        self.intel = 1
        self.damage = self.stre * 2
        self.con = 1
        self.luck = randint(0,1)
        self.life = (self.con * 3)
        self.max_life = (self.con * 3)
        self.defence = int(self.con / 3)
        self.magic_defence = int((self.intel / 3) + (self.con / 5))
        self.xp = int((self.stre + self.con + (self.defence / 2))) * 2


    def easy(self):
        self.stre += 1
        self.damage = self.stre * 2
        self.con += 3
        self.life = (self.con * 3)
        self.max_life = (self.con * 3)

    def medium(self):
        self.stre += 3
        self.damage = self.stre * 2
        self.con += 5
        self.life = (self.con * 3)
        self.max_life = (self.con * 3)
        self.xp *= 1.1

    def hard(self):
        self.stre += 5
        self.damage = self.stre * 2
        self.con += 8
        self.life = (self.con * 3)
        self.max_life = (self.con * 3)
        self.luck += 3
        self.xp *= 1.3


class medium:
    def __init__(self):
        self.stre = 3
        self.dex = 3
        self.intel = 1
        self.damage = self.stre * 2
        self.con = 5
        self.life = (self.con * 3)
        self.max_life = (self.con * 3)
        self.defence = int(self.con / 3)
        self.magic_defence = int((self.intel / 3) + (self.con / 5))
        self.luck = randint(0, 2)
        self.xp = int((self.stre + self.con + (self.defence / 2))) * 2

    def easy(self):
        self.stre += 3
        self.damage = self.stre * 2
        self.con += 8
        self.life = (self.con * 3)
        self.max_life = (self.con * 3)

    def medium(self):
        self.stre += 6
        self.damage = self.stre * 2
        self.con += 10
        self.life = (self.con * 3)
        self.max_life = (self.con * 3)
        self.xp *= 1.1

    def hard(self):
        self.stre += 8
        self.damage = self.stre * 2
        self.con += 11
        self.life = (self.con * 3)
        self.max_life = (self.con * 3)
        self.luck += 9
        self.xp *= 1.3
