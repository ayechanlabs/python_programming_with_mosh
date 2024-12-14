# Write a program to remove the duplicates in a list.
# Numbers = [12, 45, 32, 12, 89, 55, 12, 32]
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
not_duplicate = []

print(f'Original List: {numbers}')

index = 0
while index < len(numbers):
    count = 0
    for number in numbers:
        if number == numbers[index]:
            count += 1

    if count <= 1:
        not_duplicate.append(numbers[index])

    index += 1

print('After Removing Duplicate Values - ')
print(not_duplicate)
