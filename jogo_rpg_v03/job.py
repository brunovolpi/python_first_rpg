from random import randint

def role_start():
    name = input('Tell me how do you want to bel called:')
    print()
    choice = input('Pick up a role:'
                   '\nWarrior: [w/W]')
    if choice == 'w' or choice == 'W':
        character = warrior(name)
        return character
    else:
        while choice != 'w' and choice != 'W':
            choice = input('Try again:'
                           '\nWarrior: [w/W]')

#a big fat __init__ so a newbie coder can call his attributes all around, sorry for that
class warrior:
    def __init__(self, name):
        self.name = name
        self.job = 'warrior'
        self.con = 5
        self.life = self.con * 5
        self.max_life = self.con * 5
        self.stre = 3
        self.intel = 1
        self.dex = 2
        self.luck = randint(0, 3)
        self.level = 0
        self.xp = self.level * 20
        self.special_skill = []
        self.skill_lenght = len(self.special_skill)
        self.special_punch = 0
        self.special_kick = 0
        self.special_rumble = 0
        self.skill_modifier = ''

#some character vision
    def print_stats(self):
        print(f'\nName: {self.name}'
              f'\nJob: {self.job}'
              f'\n'
              f'\n=== Stats ==='
              f'\nStrenght: {self.stre}'
              f'\nIntelligence: {self.intel}'
              f'\nDexterity: {self.dex}'
              f'\nLuck: {self.luck}'
              f'\n'
              f'\n=== Info ==='
              f'\nHP: {self.life}/{self.max_life}'
              f'\nLevel: {self.level}'
              f'\nXP: {self.xp}')

                        ###################### ATTACKS ######################
#basic/upgraded kick attack
    def kick_attack(self):
        kick = self.stre * 1.5
        if self.special_kick == 1:
            if self.skill_modifier == 'cc' or self.skill_modifier == 'CC':
                chance = randint(0, 100)
                if chance <= 20:
                    print('Critical hit!')
                    return int(kick) * 3
                else:
                    return int(kick)
            elif self.skill_modifier == 'di' or self.skill_modifier == 'DI':
                damage_increase = kick * 0.4
                return int(kick + damage_increase)
        else:
            return int(kick)

# basic/upgraded punch attack
    def punch_attack(self):
        punch = self.stre * 1.5
        chance = randint(0, 100)
        if self.special_punch == 1:
            if self.skill_modifier == 'dp' or self.skill_modifier == 'DP':
                if chance <= 30:
                    print('Double Punch!')
                    return int(punch * 2)
                else:
                    return int(punch)
            elif self.skill_modifier == 'tp' or self.skill_modifier == 'TP':
                if chance <= 10:
                    print('Triple Punch!')
                    return int(punch * 3)
                else:
                    return int(punch)
        elif self.special_punch == 0:
            return int(punch)

#yet to add the upgrade modifiers
    def rumble_attack(self):
        self.rumble = self.stre * 2
        self.life -= 1
        return int(self.rumble)

                        ###################### LEVEL UP ######################

    def level_up(self):  # 10 points
        self.level += 1
        self.stre += 2
        self.con += 2
        if self.level % 10 == 0:
            self.skill_upgrade_warrior()
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
                      f'\nYour Health is now: {self.life}')  # this number returns badly idk why... for now.
                if remaining_points > 0:
                    point_distribution = input(f'\n{remaining_points} points remainig to distribute:'
                                               f'\nStrenght: [s/S] - Melee Damage - 1 cost'
                                               f'\nConstitution: [c/C] - Life and Defence - 1 cost'
                                               f'\nIntelligence: [i/I] - Magic Damage - 1 cost'
                                               f'\nDexterity: [d/D] - Ranged Damage - 1 cost'
                                               f'\nLuck: [l/L] - Overall Luck - 1 cost')
                else:
                    print('No more points to distribute!')

                        ###################### JOB UPGRADE ######################

    def job_upgrade(self):
        print(f'Congratulations once again, {self.name}!'
              f'\nYou really are advancing in this game.'
              f'\nGuess what! Its time to upgrade your role!'
              f'\n')
        role_choice = input('For Warrior there are 3 paths:'
                            '\nPaladin: High HP, good Defence, Harmonic Spells, Constitution/Intelligence bonus'
                            '\n'
                            '\nBrute: High HP, good Offence, Enforce Spells, Strenght/Constitution bonus'
                            '\n'
                            '\nMongrel: High Offence, good  HP, Enforce Spells, Strenght/Dexterity bonus'
                            '\n'
                            '\nEach role has their own benefits, make your pick:'
                            '\nPaladin: [p/P]'
                            '\nBrute: [b/B]'
                            '\nMongrel: [m/M]')
        if role_choice == 'p' or role_choice == 'P':
            print('You are now a Paladin, prepare for a 20 points stat boost!')
            #20 points
            self.con += 3
            self.intel += 2
            self.job = 'paladin'
            remaining_points = 15
            point_distribution = input(f'You changed your role!'
                                       f'\n20 points gained, 5 points are obligatory to Constitution and Intelligence for Paladin role'
                                       f'\n15 points remainig to distribute:'
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
                          f'\nYour Health is now: {self.life}')  # this number returns badly idk why... for now.
                    if remaining_points > 0:
                        point_distribution = input(f'\n{remaining_points} points remainig to distribute:'
                                                   f'\nStrenght: [s/S] - Melee Damage - 1 cost'
                                                   f'\nConstitution: [c/C] - Life and Defence - 1 cost'
                                                   f'\nIntelligence: [i/I] - Magic Damage - 1 cost'
                                                   f'\nDexterity: [d/D] - Ranged Damage - 1 cost'
                                                   f'\nLuck: [l/L] - Overall Luck - 1 cost')
                    else:
                        print('No more points to distribute!')
        elif role_choice == 'b' or role_choice == 'B':
            print('You are now a Brute, prepare for a stat boost!')
            self.con += 2
            self.stre += 3
            self.job = 'brute'
            remaining_points = 15
            point_distribution = input(f'You changed your role!'
                                       f'\n20 points gained, 5 points are obligatory to Strenght and Constitution for Brute role'
                                       f'\n15 points remainig to distribute:'
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
                          f'\nYour Health is now: {self.life}')  # this number returns badly idk why... for now.
                    if remaining_points > 0:
                        point_distribution = input(f'\n{remaining_points} points remainig to distribute:'
                                                   f'\nStrenght: [s/S] - Melee Damage - 1 cost'
                                                   f'\nConstitution: [c/C] - Life and Defence - 1 cost'
                                                   f'\nIntelligence: [i/I] - Magic Damage - 1 cost'
                                                   f'\nDexterity: [d/D] - Ranged Damage - 1 cost'
                                                   f'\nLuck: [l/L] - Overall Luck - 1 cost')
                    else:
                        print('No more points to distribute!')
            #print stats and define bonus
            self.job = 'brute'
        elif  role_choice == 'm' or role_choice == 'M':
            print('You are now a Brute, prepare for a stat boost!')
            self.stre += 3
            self.dex += 2
            self.job = 'mongrel'
            remaining_points = 15
            point_distribution = input(f'You changed your role!'
                                       f'\n20 points gained, 5 points are obligatory to Strenght and Dexterity for Mongrel role'
                                       f'\n15 points remainig to distribute:'
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
                          f'\nYour Health is now: {self.life}')  # this number returns badly idk why... for now.
                    if remaining_points > 0:
                        point_distribution = input(f'\n{remaining_points} points remainig to distribute:'
                                                   f'\nStrenght: [s/S] - Melee Damage - 1 cost'
                                                   f'\nConstitution: [c/C] - Life and Defence - 1 cost'
                                                   f'\nIntelligence: [i/I] - Magic Damage - 1 cost'
                                                   f'\nDexterity: [d/D] - Ranged Damage - 1 cost'
                                                   f'\nLuck: [l/L] - Overall Luck - 1 cost')
                    else:
                        print('No more points to distribute!')
            self.job = 'mongrel'

                        ###################### SKILL UPGRADE SYSTEM ######################

                        ###################### SKILL UPGRADE ######################

    def skill_upgrade_warrior(self):
        self.special_skill += 1
        self.special_skill.append(0)
        if self.skill_lenght == 1:
            skill_choice = input(f'Congratulations! You are now lvl {self.level}!'
                                 '\nThat means you gained +1 Special Skill point!'
                                 '\nIts time to choose a skill to upgrade:'
                                 '\nKick: [k/K] (20% Critical chance /OR/ +40% Damage Increase)'
                                 '\nPunch: [p/P] (30% Double Punch chance /OR/ 20% Dodge chance)'
                                 '\nRumble: [r/R] (25% Stun chance /OR/ 10% Combo chance)')
            if skill_choice == 'k' or skill_choice == 'K':
                modifier_choice = input('You have upgraded your Kick skill!'
                                        '\nNow into your skill can be attached a modifier!'
                                        '\n'
                                        '\nChoose a modifier for the skill: '
                                        '\nCritical Chance (20%): [cc/CC]'
                                        '\nDamage Increase (+40%): [di/DI]')
                if modifier_choice == 'cc' or modifier_choice == 'CC':
                    self.special_skill -= 1
                    self.special_kick += 1
                    self.skill_modifier += f'{modifier_choice}'
                    print('Now Kick attack has 20% critical chance (3x damage)!')
                elif modifier_choice == 'di' or modifier_choice == 'DI':
                    self.special_skill -= 1
                    self.special_kick += 1
                    self.skill_modifier += f'{modifier_choice}'
                    print('Now Kick attack has +40% damage!')
            elif skill_choice == 'p' or skill_choice == 'P':
                modifier_choice = input('You have upgraded your Punch skill!'
                                        '\nNow into your skill can be attached a modifier!'
                                        '\n'
                                        '\nChoose a modifier for the skill: '
                                        '\nDouble Punch chance! (30%): [dp/DP]'
                                        '\nTriple Punch chance! (10%): [tp/TP]')
                if modifier_choice == 'tp' or modifier_choice == 'TP':
                    self.special_skill -= 1
                    self.special_punch += 1
                    self.skill_modifier += f'{modifier_choice}'
                    print('Now your Punch attack has 30% of double damage!')
                elif modifier_choice == 'dp' or modifier_choice == 'DP':
                    self.special_skill -= 1
                    self.special_punch += 1
                    self.skill_modifier += f'{modifier_choice}'
            elif skill_choice == 'r' or skill_choice == 'R':
                modifier_choice = input('You have upgraded your Rumble skill!'
                                        '\nNow into your skill can be attached a modifier!'
                                        '\n'
                                        '\nChoose a modifier for the skill:'
                                        '\nStun chance! (25%): [s/S]'
                                        '\nCombo chance! (10%): [c/C]')
                if modifier_choice == 's' or modifier_choice == 'S':
                    self.special_skill -= 1
                    print('Now your Rumble attack has 25% stun chance!')
            else:
                while skill_choice != 'k' and skill_choice != 'K' and skill_choice != 'p' and skill_choice != 'P' and skill_choice != 'r' and skill_choice != 'R':
                    skill_choice = input('Sorry, type again!'
                                         '\nKick: [k/K] (20% Critical chance /OR/ +40% Damage Increase)'
                                         '\nPunch: [p/P] (30% Double Punch chance /OR/ 20% Dodge chance)'
                                         '\nRumble: [r/R] (25% Stun chance /OR/ 10% Combo chance)')
        elif self.skill_lenght == 2:
            skill_choice = input(f'Congratulations! You are now lvl {self.level}!'
                                 '\nThat means you gained +1 Special Skill point!'
                                 '\nIts time to choose a skill to upgrade:'
                                 '\nKick: [k/K] (20% Critical chance /OR/ +40% Damage Increase)'
                                 '\nPunch: [p/P] (30% Double Punch chance /OR/ 20% Dodge chance)'
                                 '\nRumble: [r/R] (25% Stun chance /OR/ 10% Combo chance)')
            if skill_choice == 'k' or skill_choice == 'K':
                modifier_choice = input('You have upgraded your Kick skill!'
                                        '\nNow into your skill can be attached a modifier!'
                                        '\n'
                                        '\nChoose a modifier for the skill: '
                                        '\nCritical Chance (20%): [cc/CC]'
                                        '\nDamage Increase (+40%): [di/DI]')
                if modifier_choice == 'cc' or modifier_choice == 'CC':
                    self.special_skill -= 1
                    print('Now Kick attack has 20% critical chance (3x damage)!')
                    critical_chance = randint(0, 100)
                    if critical_chance <= 20:
                        self.kick = (self.stre * 2) * 3
                elif modifier_choice == 'di' or modifier_choice == 'DI':
                    self.special_skill -= 1
                    print('Now Kick attack has +40% damage!')
                    self.kick = (self.stre * 2) + (self.stre * 0.4)
            elif skill_choice == 'p' or skill_choice == 'P':
                modifier_choice = input('You have upgraded your Punch skill!'
                                        '\nNow into your skill can be attached a modifier!'
                                        '\n'
                                        '\nChoose a modifier for the skill: '
                                        '\nDouble Punch chance! (30%): [dp/DP]'
                                        '\nDamage + Dodge chance! (+20%): [dd/DD]')
                if modifier_choice == 'dp' or modifier_choice == 'DP':
                    self.special_skill -= 1
                    print('Now your Punch attack has 30% of double damage!')
                    double_damage_chance = randint(0, 100)
                    if double_damage_chance <= 30:
                        self.punch = (self.stre * 1.5) * 2
                    else:
                        self.special_skill -= 1
                        self.punch = self.stre * 1.5
            elif skill_choice == 'r' or skill_choice == 'R':
                modifier_choice = input('You have upgraded your Rumble skill!'
                                        '\nNow into your skill can be attached a modifier!'
                                        '\n'
                                        '\nChoose a modifier for the skill:'
                                        '\nStun chance! (25%): [s/S]'
                                        '\nCombo chance! (10%): [c/C]')
                if modifier_choice == 's' or modifier_choice == 'S':
                    self.special_skill -= 1
                    print('Now your Rumble attack has 25% stun chance!')
            else:
                while skill_choice != 'k' and skill_choice != 'K' and skill_choice != 'p' and skill_choice != 'P' and skill_choice != 'r' and skill_choice != 'R':
                    skill_choice = input('Sorry, type again!'
                                         '\nKick: [k/K] (20% Critical chance /OR/ +40% Damage Increase)'
                                         '\nPunch: [p/P] (30% Double Punch chance /OR/ 20% Dodge chance)'
                                         '\nRumble: [r/R] (25% Stun chance /OR/ 10% Combo chance)')
        elif self.skill_lenght == 3:
            self.job_upgrade()

