"""
In this exercise, we are going to learn about Python strings.
In order to define a string in python, we can use both single quotes and double
quotes to define a string.
But there are times you have to use a specific form.
Normally we use single/double quote/s to define a short string but what if
we want to write or make a string of multiple lengths. Like a message that
we use it to send in email, then we can use triple quotes.

In python, we can use square brackets to get the index of the string or
character of the string.
"""

short_msg = 'Python for Beginners'
print(short_msg)

short_msg1 = "Python's Course for Beginners"
print(short_msg1)

short_msg2 = 'Python for "Beginners"'
print(short_msg2)

email_msg = '''Hi Alex,
Here is our first email to you.
Thank you,
The support team
'''
print(email_msg)

course = 'Python for Beginners'
print(course[0])  # index of the 1st character is zero
print(course[-1])  # index of the last character
print(course[-2])  # index of the second last character
print(course[0:3])  # it will generate a string from a string
print(course[:])  # it has default value of start (which is zero) and end (which is length of characters) index
print(course[0:])  # it will start from zero up to length of characters
print(course[1:])  # it will start from one up to length of characters
print(course[:5])  # it will start from zero up to index of 5.

