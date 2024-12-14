"""
Now so far, we've been writing all our code right here, in one file.
But as our programs grow, we need a better way to organize our code.
We need to break up our code into smaller, more manageable and more
maintainable chunks which we call functions.

What is a function?
A function is a container for a few lines of code that perform a specific
task.
"""

# greet_user() # error

def greet_user():
    print('Hi there!')
    print('Welcome aboard.')

# in here, we've to note that the order of code executed line by line.
# we can't call 'greet_user()' method before we declare it.
print("Start")
greet_user()
print("Finish")

