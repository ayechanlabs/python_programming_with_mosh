"""
In this exercise, we are going to learn about the things that we can do with
strings.
We also call the functions of the string or in our python language as a method
which is common term in OOP(Object-Oriented Programming)
But the difference between functions and methods are that:
functions aren't belong to strings, numbers or any other kinds of objects.
whereas methods are belong to one specific objects such as string, numbers.
For Example, print(), input(), len() are general purpose functions and
upper() is specific to string which we refer to as a method.
"""

course = 'Python for Beginners'

# len(), will calculate the numbers of characters in the string.
print(len(course))

# upper(), will convert the string to uppercase letter.
# Note: the upper() doesn't change or modify our original string.
# it creates a new string and convert it to uppercase and returns it.
print(course.upper())

# lower(), will convert the string to lowercase letter, similar to upper()
# method.
print(course.lower())

# if you want to find a character or a sequence of characters in a string.
# in those situations, we can use find() method.
# this will return the index of the first occurrence of character 'P' in our string.
print(course.find('P'))
# this will return the result as "-1" bcoz we don't have that character in our string.
print(course.find("O"))  # -1
# this will return the index number of a starting sequence. for example, if the character 'B' is at index 11 which is starting letter of a word.
print(course.find("Beginners"))
# find() method is also case-sensitive language, which means if we pass same character or a sequence of character in different case it will not know it.
print(course.find('beginners'))

# if you want to change a character or a sequence of character in a string, we've a method called replace().
print(course.replace('Beginners', 'Absolute Beginners'))
# same as find(), replace() is also case-sensitive method.
print(course.replace('beginners', "Absolute Beginners"))
# we can also replace a single character from the string.
print(course.replace('P', 'J'))

# there are times we want to check our character or a sequence of characters in our string.
# In those situations, we can use 'in' operators.
# this expression will produce a boolean value
print('Python' in course)  # true

print('python' in course)  # false, bcoz we don't have exact sequence of character in our string

"""
We've to note that the difference between find() and in() are that
in find() it will return the index of that character or a sequence of characters, whereas in() will return the boolean result of that character or a sequence of character.

len()
upper()
lower()
title()
capitalize()
find()
replace()
'....' in string
"""
