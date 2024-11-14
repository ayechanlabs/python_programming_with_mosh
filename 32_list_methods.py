"""
In this exercise, we're going to talk about list methods (or) functions.
These are operations that we can perform on a list.
"""
numbers = [5, 2, 1, 7, 4]
print('Original List:', numbers)

# append a new item to a list
numbers.append(20) # this new item will add at the end of the list
print(numbers)

# let's say, we want to insert an item at the start/ middle or end of the
# list. we can use insert() method.
# insert(): add a new item to a list to a specific location or index
# insert(index, value)
numbers.insert(0, 10)
print(numbers)

# let's say, we want to remove an item from the list. we can use remove()
# method.
# remove(): remove an item from a list
# remove(value)
numbers.remove(1)
print(numbers)

