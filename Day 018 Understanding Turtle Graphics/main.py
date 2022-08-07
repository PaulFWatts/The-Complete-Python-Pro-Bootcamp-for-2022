from turtle import Screen, Turtle

print("\033[2J\033[1;1H")  # clear terminal
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("coral")
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)


screen = Screen()
screen.exitonclick()
