def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------------------------')
    print('             JOURNAL')
    print('-----------------------------------')
    print()


def run_event_loop():

    print('What would you like to do in your journal?')
    print()

    cmd = None

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries()
        elif cmd == 'a':
            add_entry()
        elif cmd != 'x':
            print("Sorry, I don't understand command: {}.".format(cmd))
    
    print()
    print('Goodbye.')
    print()


def list_entries():
    print('Listing...')


def add_entry():
    print('Adding...')


main()