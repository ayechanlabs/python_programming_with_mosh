"""
In this exercise, we are going to look at formatted string.
Formatted string are useful when we want to dynamically generate text with
our variables.
To define formatted string, we've to prefix our string with a 'f' followed by
single/double quotes.
Inside formatted string, we can type the message that we want to print, and we
can use curly brackets {} to define the variable inside our formatted string.
"""

first_name = "John"
last_name = "Smith"

# while this approach perfectly works, it's not ideal because when our text
# gets more complicated it becomes harder to visualize the output.
# That's why, we use formatted string which is easy to visualize the output.
message = first_name + ' [' + last_name + '] is a coder.'
print(message)

msg = f"{first_name} [{last_name}] is a coder."
print(msg)
