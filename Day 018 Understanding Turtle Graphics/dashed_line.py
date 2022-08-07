from turtle import Screen, Turtle


print("\033[2J\033[1;1H")  # clear terminal
tim = Turtle()
tim.color("coral")
tim.hideturtle()

########### Challenge 2 - Draw a Dashed Line ########
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()