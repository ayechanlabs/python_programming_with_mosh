"""
In this exercise, let's learn about 'Dictionaries'.
We use 'dictionaries' to store information that comes as key value pairs.
Let's see an example. A customer has so many data, such as name, email and
phone, etc.

key:    value
Name: John
Email: john@gmail.com
Phone: 0123456789
"""
# customer = {} # <- empty dictionaries

# key has to be unique, we can't use duplicate keys.
customer = {
    "name": "john",
    "age": 30,
    "is_verified": True
}

# we can get a value from dictionaries by calling the key
# customer[key] = (value) <- output
print(customer['name']) # john

# if we pass a key that doesn't exist, then we will get an error.
# print(customer['birthdate']) # error
# print(customer['Name']) # also error, python is case-sensitive.

# to avoid the key mistake, we can use get() method.
print(customer.get("Name")) # get None, instead of key error
print(customer.get("name")) # john

# we can also give default value if the key is not found
print(customer.get("Name", "Alex"))

# we can also update the value using a key.
customer["name"] = 'Aye Chan'
print(customer.get('name'))

# we can easily also add new key: value pairs to the dictionaries
customer["birthdate"] = "Apr 5 1998"
print(customer["birthdate"])

