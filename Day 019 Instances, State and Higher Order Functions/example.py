from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


print("\033[2J\033[1;1H")  # clear terminal


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
