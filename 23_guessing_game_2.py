secret_num = 9
guess_count = 0
guess_limit = 3
is_correct = False

while guess_count < guess_limit and not is_correct:
    guess_num = int(input("Guess: "))

    if guess_num == secret_num:
        print("You won!")
        is_correct = True
    else:
        guess_count = guess_count + 1

if not is_correct:
    print("Sorry! you failed!")
