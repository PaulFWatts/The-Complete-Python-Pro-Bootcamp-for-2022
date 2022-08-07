programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "A repetition of a block of code.", }

# Retrieving items from a dictionary
# print(programming_dictionary["Bug"])

# Adding items to a dictionary
programming_dictionary["Variable"] = "A name that you give to a value."
# print(programming_dictionary)

# Creating an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary.clear()
# print(programming_dictionary)

# Edit an item in a dictionary (will add a new value if the key doesn't exist)
# programming_dictionary["Bug"] = "A moth in your computer."

# Delete an item from a dictionary
# programming_dictionary.pop("Bug")

# Looping through a dictionary
for key, value in programming_dictionary.items():
    print(key, " - ", value)
