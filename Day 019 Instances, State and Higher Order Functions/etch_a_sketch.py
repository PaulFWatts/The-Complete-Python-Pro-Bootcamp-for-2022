from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()
tim.color("coral")


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


print("\033[2J\033[1;1H")  # clear terminal

screen.listen()
screen.onkey(move_forwards, "Right")
screen.onkey(move_backwards, "Left")
screen.onkey(turn_left, "Up")
screen.onkey(turn_right, "Down")
screen.onkey(clear, "c")

screen.exitonclick()
