from random import randint

def job_choice():
    name = input('Whats your name?')
    character = input('Choose your class!'
                      '\nWarrior: [w/W]'
                      '\nMage: [m/M]'
                      '\nArcher: [a/A]')
    if character == 'w' or character == 'W':
        character = warrior(name)
        print('You are now a Warrior!')
        return character
    elif character == 'm' or character == 'M':
        character = mage(name)
        print('You are now a Mage!')
        return character
    #if character == 'm' or character == 'M':
     #   character = mage(name)

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
        self.special_skill = 0

    def skill_upgrade_warrior(self):
        self.special_skill += 1
        skill_choice = input('Congratulations! You are now lvl 10!'
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
        if skill_choice == 'p' or skill_choice == 'P':
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
        if skill_choice == 'r' or skill_choice == 'R':
            modifier_choice = input('You have upgraded your Rumble skill!'
                                    '\nNow into your skill can be attached a modifier!'
                                    '\n'
                                    '\nChoose a modifier for the skill:'
                                    '\nStun chance! (25%): [s/S]'
                                    '\nCombo chance! (10%): [c/C]')
            if modifier_choice == 's' or modifier_choice == 'S':
                self.special_skill -= 1
                print('Now your Rumble attack has 25% stun chance!')
                stun_chance = randint(0, 100)
               # if stun_chance <= 25:
                #    self.rumble

    def stored_special_points(self):
        self.special_points = 0

    def kick_attack(self):
        self.kick = self.stre * 1.5

    def skill_modifier(self):
        skill_choice = input('Congratulations! You are now lvl 10!'
                             '\nThat means you gained +1 Special Skill point!'
                             '\nIts time to choose a skill to upgrade:'
                             '\nKick: [k/K] (20% Critical chance /OR/ +40% Damage Increase)'
                             '\nPunch: [p/P] (30% Double Punch chance /OR/ 20% Dodge chance)'
                             '\nRumble: [r/R] (25% Stun chance /OR/ 10% Combo chance)')
        if skill_choice == 'k' or skill_choice == 'K':
            self.kick_modifier()
        while skill_choice != 'k' and skill_choice != 'K' and skill_choice != 'p' and skill_choice != 'P' and skill_choice != 'r' and skill_choice != 'R':
            skill_choice = input('Try again!'
                                 '\nKick: [k/K] (20% Critical chance /OR/ +40% Damage Increase)'
                                 '\nPunch: [p/P] (30% Double Punch chance /OR/ 20% Dodge chance)'
                                 '\nRumble: [r/R] (25% Stun chance /OR/ 10% Combo chance)')

            if skill_choice == 'k' or skill_choice == 'K':
                self.kick_modifier()

    def kick_modifier(self):
        skill_choice = input('Your choice is the Kick skill!'
                                '\nNow into your skill can be attached a modifier!'
                                '\n'
                                '\nChoose a modifier for the skill: '
                                '\nCritical Chance (20%): [cc/CC]'
                                '\nDamage Increase (+40%): [di/DI]')
        if skill_choice == 'cc' or skill_choice == 'CC':
            self.special_skill -= 1
            print('Now Kick attack has 20% critical chance (3x damage)!')


    def kick_attack(self):
        self.kick = self.stre * 1.5


        critical_chance = randint(0, 100)
        if critical_chance <= 20:
            self.kick = (self.stre * 1.5) * 3
            return int(self.kick)
        else:
            self.kick = self.stre * 1.5
            return int(self.kick)

    def skill_attack(self):
        self.kick_modifier() #Chance to miss
        self.punch = self.stre * 1.5
        self.rumble = self.stre * 2 #-1 HP
        skill_use = input('Choose your movement!'
                              '\nKick: [k/K]'
                              '\nPunch: [p/P]'
                              '\nRumble: [r/R]')
        if skill_use == 'k' or skill_use == 'K':
            chance = randint(0, 100)
            if chance > 80:
                print()
                print('Kick attack has missed!')
                return 0
            else:
                return int(self.kick_modifier())
        elif skill_use == 'p' or skill_use == 'P':
            return int(self.punch)
        elif skill_use == 'r' or skill_use == 'R':
            self.life -= 1
            return int(self.rumble)



                        ###################### LEVEL UP #######################

    def level_up(self): #10 points
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
                    if self.level >= 10:
                        self.skill_upgrade_warrior()

    def att_print(self):
        print(f'Life: {self.life}'
              f'\nLevel: {self.level}')

class mage:
    def __init__(self, name):
        self.name = name
        self.con = 2
        self.life = (self.con * 4)
        self.max_life = (self.con * 4)
        self.stre = 1
        self.intel = 5
        self.dex = 1
        self.luck = randint(0, 3) + 2
        self.mana = self.intel * 6
        self.level = 0
        self.xp = self.level * 20
        self.job = 'mage'
        self.special_skill = 0

    def melee_moves(self):
        self.kick = self.stre * 2  # Chance to miss
        self.punch = self.stre * 1.5
        skill_use = input('Choose your movement!'
                              '\nKick: [k/K]'
                              '\nPunch: [p/P]')
        if skill_use == 'k' or skill_use == 'K':
            chance = randint(0, 100)
            if chance > 80:
                print()
                print('Kick attack has missed!')
                return 0
            else:
                return int(self.kick)
        elif skill_use == 'p' or skill_use == 'P':
            return int(self.punch)

    def harmonic_magic(self):
        self.heal = int(self.intel * 1.2)
        skill_use = input('Choose your harmonic spell!'
                          '\nHeal: [h/H]')
        while skill_use != 'h' and skill_use != 'H':
            skill_use = input('Sorry, no valid answer typed, try again!'
                              '\nHeal: [h/H]')
            if skill_use == 'h' or skill_use == 'H':
                return int(self.heal)
        if skill_use == 'h' or skill_use == 'H':
            return int(self.heal)

    def chaos_magic(self):
        self.burn = self.intel * 3
        self.freeze = self.intel * 3
        skill_use = input('Choose your chaotic spell!'
                          '\nBurn (-5 mana): [b/B]'
                          '\nFreeze (´5 mana): [f/F]')
        while skill_use != 'b' and skill_use != 'B' and skill_use != 'f' and skill_use != 'F':
            if skill_use == 'b' or skill_use == 'B':
                return int(self.burn)
            elif skill_use == 'f' or skill_use == 'F':
                return int(self.burn)
            skill_use = input('Sorry, no valid option typed, try again!'
                              '\nBurn (-5 mana): [b/B]'
                              '\nFreeze (-5 mana): [f/F]')
        if skill_use == 'b' or skill_use == 'B':
            self.mana -= 5
            return int(self.burn)
        elif skill_use == 'f' or skill_use == 'F':
            self.mana -= 5
            return int(self.burn)


    def att_print(self):
        print(f'===== Player ====='
              f'\nHP: {self.life}/{self.max_life}'
              f'\nMana: {self.mana}'
              f'\nXP: {self.xp}')
    #need to set skill upgrading to mage context
    def level_up(self): #10 points
        self.level += 1
        self.intel += 3
        self.con += 1
        self.life -= 1
        if self.level >= 10:
            self.skill_upgrade()
        remaining_points = 6
        point_distribution = input(f'You leveled up!'
                                    f'\n10 points gained, 4 points are obligatory to Intelligence and Constitution for Mage job'
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
                    if self.level >= 10:
                        self.skill_upgrade_mage()

    def skill_upgrade_mage(self):
        skill_choice = input('Congratulations! You are now lvl 10!'
                             '\nIts time to choose a skill to upgrade:'
                             '\nKick: [k/K]'
                             '\nPunch: [p/P]'
                             '\nBurn: [b/B]'
                             '\nFreeze: [f/F]'
                             '\nHeal: [h/H]')
        if skill_choice == 'k' or skill_choice == 'K':
            modifier_choice = input('You have upgraded your Kick skill!'
                  '\nNow into your skill can be attached a modifier!'
                  '\n'
                  '\nChoose a modifier for the skill: '
                                   '\nCritical Chance (20%): [cc/CC]'
                                   '\nDamage Increase (+40%): [di/DI]')
            if modifier_choice == 'cc' or modifier_choice == 'CC':
                print('Now Kick attack has 20% critical chance (3x damage)!')
                critical_chance = randint(0, 100)
                if critical_chance <= 20:
                    self.kick = (self.stre * 2) * 3
            elif modifier_choice == 'di' or modifier_choice == 'DI':
                print('Now Kick attack has +40% damage!')
                self.kick = (self.stre * 2) + (self.stre * 0.4)
        if skill_choice == 'p' or skill_choice == 'P':
            modifier_choice = input('You have upgraded your Punch skill!'
                                    '\nNow into your skill can be attached a modifier!'
                                    '\n'
                                    '\nChoose a modifier for the skill: '
                                    '\nDouble Punch chance! (30%): [dp/DP]'
                                    '\nDamage + Dodge chance! (+20%): [dd/DD]')
            if modifier_choice == 'dp' or modifier_choice == 'DP':
                print('Now your Punch attack has 30% of double damage!')
                double_damage_chance = randint(0, 100)
                if double_damage_chance <= 30:
                    self.punch = (self.stre * 1.5) * 2
                else:
                    self.punch = self.stre * 1.5
        if skill_choice == ''