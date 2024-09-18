# Using 'while-else' condition along with 'break' statement
secret_num = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess_num = int(input("Guess: "))

    if guess_num == secret_num:
        print("You won!")
        break
    else:
        guess_count = guess_count + 1
else:
    print("Sorry, you failed!")
