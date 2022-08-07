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


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
