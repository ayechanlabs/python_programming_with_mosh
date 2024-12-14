phone = input("Phone: ")

num_to_words = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten"
}

words = ""
for num in phone:
    words += num_to_words.get(num, "?") + " "

print(words)
