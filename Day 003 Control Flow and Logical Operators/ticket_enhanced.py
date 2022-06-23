""" Demonstrates if /elif /else statements """

print("Welcome to the roller coaster.")
height = int(input("How tall are you in cm? \n"))

if height > 120:
    print("You're tall enough to ride the roller coaster.")
    age = int(input("How old are you? \n"))
    if age < 12:
        print("please pay $5.")
    elif age <= 18:
        print("please pay $7.")
    else:
        print("please pay $12.")
else:
    print("You're not tall enough to ride the roller coaster.")
