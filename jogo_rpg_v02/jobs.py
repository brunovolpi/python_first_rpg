from random import randint

class warrior:
    def __init__(self, name):
        self.name = name
        self.job = 'warrior'
        self.con = 5
        self.life = self.con * 5
        self.stre = 3
        self.intel = 1
        self.dex = 2
        self.luck = randint(0, 3)
        self.level = 0
        self.xp = self.level * 20

    def skill_attack(self):
        self.kick = self.stre * 2 #Chance to miss
        self.punch = self.stre * 1.5
        self.rumble = self.stre * 2 #-1 HP
        skill_use = input('Choose your movement!'
                              '\nKick: [k/K]'
                              '\nPunch: [p/P]'
                              '\nRumble: [r/R]')
        if skill_use == 'k' or skill_use == 'K':
            return int(self.kick)
        elif skill_use == 'p' or skill_use == 'P':
            return int(self.punch)
        elif skill_use == 'r' or skill_use == 'R':
            return int(self.rumble)

    def level_up(self): #10 points
        self.stre += 2
        self.con += 2
        remaining_points = 6
        point_distribution = input(f'You leveled up!'
                                    f'\n10 points gained, 4 points are obligatory to strenght and constitution for Warrior job'
                                    f'\n6 points remainig to distribute:'
                                    f'\nStrenght: [s/S] - Melee Damage - 1 cost'
                                    f'\nConstitution: [c/C] - Life and Defence - 1 cost'
                                    f'\nIntelligence: [i/I] - Magic Damage - 1 cost'
                                    f'\nDexterity: [d/D] - Ranged Damage - 1 cost'
                                    f'\nLuck: [l/L] - Overall Luck - 1 cost')
        while remaining_points > 0:
            if point_distribution == 'i' or point_distribution == 'I':
                point_quantity = int(input('Insert how many points you want in this attribute: '))
                remaining_points -= point_quantity
                self.intel += point_quantity
                print(f'You invested {point_quantity} points in Intelligence attribute!'
                      f'\nYour actual Intelligence is: {self.intel}')
                if remaining_points > 0:
                    point_distribution = input(f'\n{remaining_points} points remainig to distribute:'
                                    f'\nStrenght: [s/S] - Melee Damage - 1 cost'
                                    f'\nConstitution: [c/C] - Life and Defence - 1 cost'
                                    f'\nIntelligence: [i/I] - Magic Damage - 1 cost'
                                    f'\nDexterity: [d/D] - Ranged Damage - 1 cost'
                                    f'\nLuck: [l/L] - Overall Luck - 1 cost')
                else:
                    print('No more points to distribute!')
            elif point_distribution == 'd' or point_distribution == 'D':
                point_quantity = int(input('Insert how many points you want in this attribute: '))
                remaining_points -= point_quantity
                self.dex += point_quantity
                print(f'You invested {point_quantity} points in Dexterity attribute!'
                      f'\nYour actual Dexterity is: {self.dex}')
                if remaining_points > 0:
                    point_distribution = input(f'\n{remaining_points} points remainig to distribute:'
                                    f'\nStrenght: [s/S] - Melee Damage - 1 cost'
                                    f'\nConstitution: [c/C] - Life and Defence - 1 cost'
                                    f'\nIntelligence: [i/I] - Magic Damage - 1 cost'
                                    f'\nDexterity: [d/D] - Ranged Damage - 1 cost'
                                    f'\nLuck: [l/L] - Overall Luck - 1 cost')
                else:
                    print('No more points to distribute!')
            elif point_distribution == 'l' or point_distribution == 'L':
                point_quantity = int(input('Insert how many points you want in this attribute: '))
                remaining_points -= point_quantity
                self.luck += point_quantity
                print(f'You invested {point_quantity} points in Luck attribute!'
                      f'\nYour actual Luck is: {self.luck}')
                if remaining_points > 0:
                    point_distribution = input(f'\n{remaining_points} points remainig to distribute:'
                                    f'\nStrenght: [s/S] - Melee Damage - 1 cost'
                                    f'\nConstitution: [c/C] - Life and Defence - 1 cost'
                                    f'\nIntelligence: [i/I] - Magic Damage - 1 cost'
                                    f'\nDexterity: [d/D] - Ranged Damage - 1 cost'
                                    f'\nLuck: [l/L] - Overall Luck - 1 cost')
            elif point_distribution == 's' or point_distribution == 'S':
                point_quantity = int(input('Insert how many points you want in this attribute: '))
                remaining_points -= point_quantity
                self.stre += point_quantity
                print(f'You invested {point_quantity} points in Strenght attribute!'
                      f'\nYour actual Strenght is: {self.stre}')
                if remaining_points > 0:
                    point_distribution = input(f'\n{remaining_points} points remainig to distribute:'
                                    f'\nStrenght: [s/S] - Melee Damage - 1 cost'
                                    f'\nConstitution: [c/C] - Life and Defence - 1 cost'
                                    f'\nIntelligence: [i/I] - Magic Damage - 1 cost'
                                    f'\nDexterity: [d/D] - Ranged Damage - 1 cost'
                                    f'\nLuck: [l/L] - Overall Luck - 1 cost')
            elif point_distribution == 'c' or point_distribution == 'C':
                point_quantity = int(input('Insert how many points you want in this attribute: '))
                remaining_points -= point_quantity
                self.con += point_quantity
                print(f'You invested {point_quantity} points in Constitution attribute!'
                      f'\nYour actual Constitution is: {self.con}'
                      f'\nYour Health is now: {self.life}') #this number returns badly idk why... for now.
                if remaining_points > 0:
                    point_distribution = input(f'\n{remaining_points} points remainig to distribute:'
                                    f'\nStrenght: [s/S] - Melee Damage - 1 cost'
                                    f'\nConstitution: [c/C] - Life and Defence - 1 cost'
                                    f'\nIntelligence: [i/I] - Magic Damage - 1 cost'
                                    f'\nDexterity: [d/D] - Ranged Damage - 1 cost'
                                    f'\nLuck: [l/L] - Overall Luck - 1 cost')
                else:
                    print('No more points to distribute!')
    def att_print(self):
        print(f'Life: {self.life}')

class mage:
    def __init__(self, name):
        self.name = name
        self.con = 0
        self.life = self.con * 4
        self.stre = 0
        self.intel = 0
        self.dex = 0
        self.luck = 0
        self.mana = self.intel * 6
        self.level = 0
        self.xp = self.level * 20
        self.job = 'mage'
