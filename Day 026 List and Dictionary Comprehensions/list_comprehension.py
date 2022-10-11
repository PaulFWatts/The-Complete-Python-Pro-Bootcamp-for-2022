import random

# Manual way to create a new List
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# Using List Comprehension
new_list = [n + 1 for n in numbers]
print(new_list)

# Using List Comprehension with a conditional
new_list = [n + 1 for n in numbers if n % 2 == 1]
print(new_list)

# Using List Comprehension with a String
name = "Angela"
new_list = [letter for letter in name]
print(new_list)

# Using List Comprehension with a Range
new_list = [n * 2 for n in range(1, 5)]
print(new_list)

# Using List Comprehension with a Dictionary
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(1, 100) for student in names}  # random.randint(1, 100) is a random number
# between 1 and 100
print(student_scores)

long_name = [name.upper() for name in names if len(name) > 5]
print(long_name)

# Using List Comprehension with a Dictionary and a conditional
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)




