# Write a program to find the largest number and smallest number
# in a list.

numbers = [10, 4, 5, 8, 1, 3, 8, 9, 2]
largest = 0 # can also give first item of the list
smallest = numbers[0]

# Method 1
for number in numbers:
    if number > largest:
        largest = number
    elif number < smallest:
        smallest = number

print('The largest number in a list:', largest)
print('The smallest number in a list:', smallest)

# Method 2
largestNum = max(numbers)
smallestNum = min(numbers)

print(f"Largest Number: {largestNum} & Smallest Number: {smallestNum}")

