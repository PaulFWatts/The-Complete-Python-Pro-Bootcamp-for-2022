import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [
    (139, 164, 183),
    (21, 118, 177),
    (240, 213, 59),
    (204, 139, 166),
    (223, 158, 84),
    (122, 72, 98),
    (142, 20, 36),
    (20, 138, 58),
    (190, 175, 23),
    (71, 30, 36),
    (195, 72, 33),
    (225, 171, 198),
    (57, 35, 32),
    (25, 170, 184),
    (236, 85, 33),
    (7, 111, 66),
    (109, 190, 136),
    (42, 173, 81),
    (183, 94, 110),
    (188, 183, 210),
    (39, 38, 45),
    (156, 208, 216),
    (154, 213, 175),
    (241, 171, 151),
    (229, 212, 16),
    (125, 115, 160),
]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
