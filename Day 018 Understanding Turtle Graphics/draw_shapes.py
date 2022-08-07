import random
from turtle import Screen, Turtle

print("\033[2J\033[1;1H")  # clear terminal
tim = Turtle()
tim.color("coral")
tim.hideturtle()

########### Challenge 3 - Draw Shapes ########

colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
