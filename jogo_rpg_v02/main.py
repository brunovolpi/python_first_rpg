import monsters
import jobs
import combat
def main():
    player1 = jobs.job_choice()
    print(f'Welcome to my game !')
    combat.combat(player1, monsters.combat_difficult('noob'))
    player1.att_print()

main()