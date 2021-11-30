import job
import monsters
import combat

def main():
    player1 = job.role_start()
    player1.print_stats()
    combat.warrior_combat(player1, monsters.combat_difficult('noob'))

main()