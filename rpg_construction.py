from random import randint
from weapons import basic_sword
from time import sleep

def final_mage_combat(character, monster):
    print('=' * 30)
    print('======= Combat mode! =======')
    print('=' * 30)
    while character.life > 0 and monster.life > 0:
        if character.level < 5:
            combat_style = input('Melee: [m/M]'
                  '\nOffence Spells: [os/OS]')
            if combat_style == 'm' or combat_style == 'M':
                kick_chance = character.melee_mode()
                if kick_chance == 'Miss!':
                    return True
                pass #idk how to pass trough 'Miss!' and keep printing the battle status.
                monster.life -= character.melee_mode()
                print(f'Monster Life: {monster.life}')
            if monster.life > 0:
                character.life - monster.damage
                print(f'Monster Damage: {monster.damage}'
                      f'\nHP: {character.life}')
            else:
                print('You killed the monster!')
                print(f'XP gained: {monster.xp}')
                character.xp - monster.xp



def combat_non_magic(character, monster):
    print('=' * 50)
    print('=' * 18, 'Combat time!', '=' * 18)
    print('=' * 50)
    while character.life > 0 and monster.life > 0:
        print()
        monster.life -= character.attack() + monster.defense
        print()
        print(f'\nHit: {character.damage}'
              f'\nMonster HP: {monster.life}')
        print()
        sleep(0.5)
        if monster.life > 0:
            character.life -= monster.damage + character.defense
            print(f'Taken: {monster.damage}'
                  f'\nHP: {character.life}')
            print()
            sleep(0.5)
            if character.life <= 0:
                print('You are dead!')
                break
        elif monster.life <= 0:
            print('The monster is now dead...')
            character.xp -= monster.xp
            print(f'You gained: {monster.xp} XP')
            if character.xp <= 0:
                character.level_up()
                print()


#right now im trying to add the Healing Skill which appears after reaching lvl 5
#But i don't know how to use the skill and maintain the combat prints indicating the combat numbers
#So far only the non_magic classes are corresponding the fighting print sequences
def combat_mage(character, monster):
    print('=' * 50)
    print('=' * 18, 'Combat time!', '=' * 18)
    print('=' * 50)
    while character.life > 0 and monster.life > 0:
        if character.level >= 5:
            character.mage_heal()
            sleep(0.5)
        else:
            print()
            monster.life -= character.attack() + monster.defense
            print()
            print(f'Hit: {character.damage}'
                  f'\nMonster HP: {monster.life}')
            sleep(0.5)
            if monster.life > 0:
                character.life -= monster.damage + character.defense
                print(f'Taken: {monster.damage}'
                      f'\nHP: {character.life}')
                sleep(0.5)
                if character.life <= 0:
                    print('You are dead!')
                    break
            elif monster.life <= 0:
                print('The monster is now dead...')
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
        strike = self.damage * 2
        if self.level >= 5:
            self.input = input('Kick: [k/K]'
                               '\nPunch: [p/P]'
                               '\nRumble (-1 life): [r/R]'
                               '\nStrike: [s/S]')
            if self.input == 's' or self.input == 'S':
                return int(strike)
            if self.input == 'p' or self.input == 'P':
                return int(punch)
            elif self.input == 'k' or self.input == 'K':
                return int(kick)
            elif self.input == 'r' or self.input == 'R':
                self.life -= 1
                return int(rumble)
        elif self.level < 5:
            self.input = input('Kick: [k/K]'
                               '\nPunch: [p/P]'
                               '\nRumble (-1 life): [r/R]')
            if self.input == 'p' or self.input == 'P':
                return int(punch)
            elif self.input == 'k' or self.input == 'K':
                return int(kick)
            elif self.input == 'r' or self.input == 'R':
                self.life -= 1
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
        arrow_strike = self.pierce_damage * 1.5
        if self.level >= 5:
            self.input = input('Kick: [k/K]'
                               '\nPunch: [p/P]'
                               '\nStab: [s/S]'
                               '\nArrow Strike: [as/AS]')
            if self.input == 'p' or self.input == 'P':
                return int(punch)
            elif self.input == 'k' or self.input == 'K':
                return int(kick)
            elif self.input == 's' or self.input == 'S':
                if critical >= 90:
                    return stab * 2
                else:
                    return int(stab)
            elif self.input == 'as' or self.input == 'AS':
                if critical >= 80:
                    return int(arrow_strike) * 2
                else:
                    return int(arrow_strike)
        elif self.level < 5:
            self.input = input('Kick: [k/K]'
                               '\nPunch: [p/P]'
                               '\nStab: [s/S]')
            if self.input == 'p' or self.input == 'P':
                return int(punch)
            elif self.input == 'k' or self.input == 'K':
                return int(kick)
            elif self.input == 's' or self.input == 'S':
                if critical >= 90:
                    return int(stab) * 2
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

    def offence_spells(self):
        self.magic_damage = self.intel * 1.5
        burn = self.magic_damage * 1.5
        freeze = self.magic_damage * 1.5
        self.input = input('Burn: [b/B]'
                           '\nFreeze: [f/F]')
        if self.input == 'b' or self.input == 'B':
            return int(burn)
        elif self.input == 'f' or self.input == 'F':
            return int(freeze)

    def defence_spells(self):
        heal = int(self.intel / 2)
        self.input = input('Heal: [h/H]')
        if self.input == 'h' or self.input == 'H':
            self.life += heal
            print(f'Healed: {heal}'
                  f'\nHP: {self.life}')

    def melee_mode(self):
        self.damage = self.stre * 1.5
        punch = self.damage * 1.1
        kick = self.damage * 1.2
        self.input = input('Kick: [k/K]'
                           '\nPunch: [p/P]')
        if self.input == 'k' or self.input == 'K':
            kick_chance = randint(0, 10)
            if kick_chance >= 3:
                return int(kick)
                print(f'Damage: {kick}')
            else:
                print('Miss!')
        elif self.input == 'p' or self.input == 'P':
            return int(punch)




#if answer == 'offense_spells':
    #ride to offense_spells damage
#elif answer == 'defence_spells':
    #ride to defence_spells self-healing

    #heal spell solution: choose between offence and defence magic
#theres another problem: how can i spare code lines when a new skill is reached?



    def attack(self):
        self.damage = self.stre * 1.5
        self.magic_damage = self.intel * 1.5
        punch = self.damage * 1.1
        kick = self.damage * 1.2
        burn = self.magic_damage * 1.5
        heal = (self.intel / 10)
        freeze = self.magic_damage * 1.5
        if self.level >= 5:
            self.input = input('Kick: [k/K]'
                               '\nPunch: [p/P]'
                               '\nBurn: (-5 mana): [b/B]'
                               '\nFreeze: (-5 mana): [f/F]'
                               '\nHeal(-5 mana): [h/H]')
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
            elif self.input == 'h' or self.input == 'H':
                self.mana -= 5
                self.life += heal
                print(f'Healed: {heal}')
        elif self.level < 5:
            self.input = input('Kick: [k/K]'
                               '\nPunch: [p/P]'
                               '\nBurn: (-5 mana): [b/B]'
                               '\nFreeze: (-5 mana): [f/F]')
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

    def mage_heal(self):
        self.heal = self.intel / 2
        self.mana -= 5
        self.life += self.heal
        print(f'Healed: {self.heal}')


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
