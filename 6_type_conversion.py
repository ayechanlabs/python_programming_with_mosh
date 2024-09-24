birth_year = input('Birth year: ')
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)

"""
whenever we use input(), we will be asking the user to input the data.
So we will giving input to program through terminal.
So whatever we type inside the terminal, we treated it as string even if the
numbers.
in other word, the input() method takes input as a string.
so when we write like this: 2024 - birth_year, python see it as like this:
2024 - '1998', so we are doing calculation with string and integer, python
doesn't know it how to do it.

so in order to able to make calculation, we will converting string data type
to integer data type.
That's what we call it as type conversion, means we will be converting our datatype
to another datatype.

so far we've learned 2 built-in functions, that are input() and print().
We've a few more functions for converting values into different types.
So we've int() functions to convert into integer from string.
float() to convert into float from string.
bool() to convert into boolean from string.

In python, we also have to get datatype of a variable. That is type()
function.
"""