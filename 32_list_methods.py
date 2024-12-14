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

# we call also remove all the items from the list, by using clear().
# numbers.clear()
# print(numbers)

# we can also use pop() to remove the last item of the list.
numbers.pop()
print(numbers)
# we can also use index number with pop() method to remove a certain item from the list.
numbers.pop(2)
print(numbers)

# we can check the existence of the item on the list, by using index().It will the index
# number of that item.
print(numbers.index(5)) # it will the index of the item.
# print(numbers.index(2)) # if we pass an item which is not in the list, we will get the error.

# There is also another way to check the existence of an item in the list.We can use 'in' operator with strings,
# list.
# We can use 'in' operator to check the existence of character, a sequence of characters or numbers.
# It will return the result in a boolean result.
print(50 in numbers)

# We also have a method to count the occurrence of an item in the list.
# We can use count() to count the number of that item in the list.
numbers.insert(3, 5)
numbers.insert(1, 5)
# print(numbers)

print(numbers.count(5))

# We can also sort our list, using sort() method.
# print(numbers.sort())

# this will not return anything because sort()
# doesn't return anything at all.It simply sorts the list.

numbers.sort()
print(numbers)

# we can also use reverse method to reverse the order of the list.
# note that if we use reverse() on the unsorted list it will just the list backward.
# but we use that on sorted list it will return it in descending order, but actually it didn't sort in descending order.
numbers.reverse()
print(numbers)

# we can also make a copy of our list.
numbers2 = numbers.copy()
# by using copy() it will make a copy of the list which is not effected by any changes make in the original list.
numbers.append(26)

print(numbers)
print(numbers2)
