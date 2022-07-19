############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): # Change to range(1, 21) to fix bug
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
#
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[(dice_num - 1)])  # Added -1 to fix bug

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994: # Change to >= to fix bug
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") # Change to int to fix bug
# if age > 18:
# print("You can drive at age {age}.") # Change to f"You can drive at age {age}." to fix bug and indent

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # Change to = to fix bug
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) # indent to fix bug
#   print(b_list)

# mutate([1,2,3,5,8,13])
