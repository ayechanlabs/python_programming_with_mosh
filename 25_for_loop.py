"""
In python, we have for loop and while loop.
we use while loop to execute a block of code multiple times or a certain
number of times, whereas we will use for loop to iterate over items
of collections such as string(is a collection of characters) or
number of times.
"""

for char in 'Python':
    print(char) # it will print out each of character from the string

# in python, we can define list using square brackets -> []
# A list is simply a list of items, a list of numbers, a list of email, etc.
for item in ['Mosh', 'John', 'Sarah', 'Alex']:
    print(item) # it will print each name from a list in a new line

for number in [1, 2, 3, 4, 5]:
    print(number) # it will print each number from a list in a new line

# in python, we can 'range' function in for loop to iterate over a
# number of times.
# 'range()' is an object which will create a number for loop to iterate
# over.
for index in range(10):
    print(index) # it will print numbers start from 0 to 9, like 10 times

for index in range(5, 10):
    print(index) # it will start loop from number 5 up to 9

for index in range(5, 10, 2):
    # 5, 7, 9
    print(index) # it will print number from 5 but skip 2 step
