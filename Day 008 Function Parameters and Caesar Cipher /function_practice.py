""" Function Practice with Inputs"""


def greet():
    """
    This function greets the user by printing 3 strings"
    """
    print("\nHello Paul!")
    print("Hello World!")
    print("Hello Universe!\n")


def greet_with_name(name: str):
    """Function with 1 parameter"""
    print(f"Hello {name}!")
    print(f"How are you {name}?\n")


def greet_with_name_and_age(name: str, age: int):
    """Function with 2 parameters"""
    print(f"Hello {name}! You are {age} years old.")
    print(f"Bye {name}?\n")


greet()
greet_with_name("Paul")

# Pass arguments using poistional arguments
greet_with_name_and_age("Paul", 65)

# Pass arguments using keyword arguments
greet_with_name_and_age(age=65, name="Paul")


