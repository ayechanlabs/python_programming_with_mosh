cmd = ""

# while cmd != 'quit':
#     cmd = input("> ").lower()
#
#     if cmd == 'help':
#         print(
#             """start - to start the car
# stop - to stop the car
# quit - to exit""")
#     elif cmd == 'start':
#         print("Car started...Ready to go!")
#     elif cmd == 'stop':
#         print("Car stopped.")
#     elif cmd == 'quit':
#         print("Program Stopped.")
#     else:
#         print("I don't understand that...")

# Version 2
while True:
    cmd = input("> ").lower()

    if cmd == 'start':
        print("Car started...Ready to go!")
    elif cmd == 'stop':
        print("Car stopped.")
    elif cmd == 'quit':
        print('Program Stopped.')
        break
    elif cmd == 'help':
        print(
            """start - to start the car
stop - to stop the car
quit - to exit"""
        )
    else:
        print("Sorry! I don't understand that...")
