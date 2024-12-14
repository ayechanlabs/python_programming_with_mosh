"""
In this exercise, we are going to talk about 'Tuple'.
'Tuple' is similar to list, but unlike a list, we can't modify it,
add new items or can't remove existing items.

'Tuples' are immutable, means we cannot mutate or change them.
"""

# numbers = [1, 2, 3] # <- this is list
numbers = (1, 2, 3, 3, 4, 3, 4, 5)

"""
In tuple, we don't have append(), insert(), remove(), pop(), clear() methods.
It only has 2 methods: count() & index()
"""

# Indexing
print(numbers[0])

# numbers[0] = 10 # error, can't modify it.

# Count: it will count the number of times that specific number or character
# occurs in a tuple.
print(numbers.count(4))

# Index
print(numbers.index(5))

"""
So we can get only information about the tuple but not change it.
"""
