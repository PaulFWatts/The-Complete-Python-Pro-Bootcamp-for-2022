""" 
Write a function that checks whether the number passed into it is a prime number or not.
Prime numbers are numbers that can only be cleanly divided by themselves and 1.
https://en.wikipedia.org/wiki/Prime_number
"""

# Write your code below this line 👇


def prime_checker(number):
    if number == 1:
        print("It's not a prime number.")
        return
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")
    return True

# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
