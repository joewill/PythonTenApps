from actors import Wizard, Creature


def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------------------------------')
    print('                 Wizard Game')
    print('---------------------------------------------')
    print()


def game_loop():

    creatures = [Creature('Toad', 1),
                 Creature('Tiger', 12),
                 Creature('Bat', 3),
                 Creature('Dragon', 50),
                 Creature('Evil Wizard', 1000)]

    hero = Wizard('Gandolf', 75)

    while True:
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')

        if cmd == 'a':
            print('Attack')
        elif cmd == 'r':
            print('Run Away!')
        elif cmd == 'l':
            print('lookaround')
        else:
            print("Ok, exiting game....bye!")
            break


if __name__ == '__main__':
    main()
