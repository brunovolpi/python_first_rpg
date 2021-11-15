#I can try to randomize the monster that will appear by creating minimun - maximun stats
from random import randint

def combat_difficult(grade_level):
    global difficult
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
        self.damage = 0
        self.life = 0
        self.defence = 0
        self.xp = 0

    def easy(self):
        self.damage += 2
        self.life += 10
        self.defence += 1
        self.xp += 26 #(2+10+1)*2 = 26

    def medium(self):
        self.damage += 3
        self.life += 12
        self.defence += 1
        self.xp += 32

    def hard(self):
        self.damage += 4
        self.life += 15
        self.defence += 2
        self.xp += 42


class medium:
    global difficult
    difficult = randint(0, 10)

    def __init__(self):
        self.damage = 0
        self.life = 0
        self.defence = 0
        self.xp = 0

    def easy(self):
        self.damage += 5
        self.life += 15
        self.defence += 4
        self.xp += 48

    def medium(self):
        self.damage += 7
        self.life += 20
        self.defence += 4
        self.xp += 62

    def hard(self):
        self.damage += 10
        self.life += 30
        self.defence += 6
        self.xp += 92
