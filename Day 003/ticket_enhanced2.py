""" Demonstrates multiple conditional statements """

print("Welcome to the roller coaster.")
height = int(input("How tall are you in cm? \n"))
bill = 0

if height > 120:
    print("You're tall enough to ride the roller coaster.")
    age = int(input("How old are you? \n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")

else:
    print("You're not tall enough to ride the roller coaster.")
