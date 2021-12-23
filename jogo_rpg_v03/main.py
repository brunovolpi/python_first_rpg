import job
import monsters
import combat

cat_jump = ['s', 'S', 'l', 'L', 'r', 'R']

def main():
    first_choice = input('Hello and welcome to my game'
          '\nThere are some interesting systems to explore, enjoy the course-options!'
          '\n'
          '\nThere are 3 paths, make a pick:'
          '\nStraight: [s/S]'
          '\nLeft: [l/L]'
          '\nRight: [r/R]')
    player1 = job.role_start()
    player1.print_stats()

    #combat.warrior_combat(player1, monsters.combat_difficult('noob'))

main()