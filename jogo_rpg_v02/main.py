import monsters
import jobs
import combat
def main():
    name = input('Whats your name?')
    test = jobs.warrior(name)
    print(type(test))
    print(f'Welcome to my game, {test.name}!')
    combat.combat(test, monsters.combat_difficult('noob'))


main()