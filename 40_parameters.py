"""
What is the difference between greet_user() & print()?
greet_user() doesn't take any inputs from user where
print() does take an input from the user.

Parameters: are the placeholders that we define in the function definition
to receive input values from the caller.

Arguments: are the actual piece of information that we pass/supply to these
functions.
"""

# No Parameters
# def greet_user():
#     print('Hi there!')
#     print('Welcome aboard.')
    
# With Parameter/s
# def greet_user(name):
#     print(f"Hi {name}!")
#     print('Welcome aboard.')

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print('Welcome aboard.')
    

print("Start")

# greet_user()

# greet_user('John')
# greet_user('Mary')

greet_user('John', 'Smith')
greet_user('Mary', 'Brown')

print("Finish")