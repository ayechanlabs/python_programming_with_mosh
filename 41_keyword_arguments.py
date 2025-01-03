def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print('Welcome aboard.')


print("Start")

# greet_user('John', 'Smith')

# if we change the order of our arguments that we pass to the function
greet_user('Smith', 'John') # so in here 'Smith' will be assigned as first name
# and 'John' will be assigned as last name which is not correct.
# so we refer to this as positional arguments.
# because their position and order matters.

greet_user(last_name='Smith', first_name='John') # so in here, we've used
# keyword arguments. so we've explicitly specified the name of the parameter,
# and the value that we're passing to that parameter. so this is more readable
# and less error-prone.
# when we use like this we can change the order of the arguments that we pass
# to the function.

print("Finish")    

    