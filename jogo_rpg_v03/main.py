import job

def main():
    player1 = job.role_start()
    print(type(player1))
    player1.print_stats()

main()