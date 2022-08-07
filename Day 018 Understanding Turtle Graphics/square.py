from turtle import Screen, Turtle

print("\033[2J\033[1;1H")  # clear terminal
turtle = Turtle()
turtle.color("coral")
turtle.hideturtle()

########### Challenge 1 - Draw a Square ########
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)


screen = Screen()
screen.exitonclick()
