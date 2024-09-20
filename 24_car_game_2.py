cmd = ""
is_start = False
is_stop = False

while cmd != 'quit':
    cmd = input("> ").lower()

    if cmd == 'help':
        print("""start - to start the car
stop - to stop the car
quit - to exit""")

    elif cmd == 'start':

        if is_start:
            print('Car is already started.')
        else:
            print('Car started...Ready to go!')

        is_start = True

    elif cmd == 'stop':

        if is_stop:
            print('Car is already stopped.')
        else:
            print('Car stopped.')

        is_stop = True

    elif cmd == 'quit':
        print('Program Stopped.')

    else:
        print("I don't understand that...")