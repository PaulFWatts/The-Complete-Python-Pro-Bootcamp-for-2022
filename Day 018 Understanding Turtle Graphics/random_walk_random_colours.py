import random
import turtle as t

print("\033[2J\033[1;1H")  # clear terminal
tim = t.Turtle()
t.colormode(255)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


########### Challenge 4 - Draw Shapes with Random Colours ########


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
