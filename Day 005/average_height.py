""" Write a program that calculates the average student height from a List of heights"""

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])  # type: ignore
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
sum = 0
for student in student_heights:
    sum = sum + int(student)

average = sum / len(student_heights)
print(round(average))
