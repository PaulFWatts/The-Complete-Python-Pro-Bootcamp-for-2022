""" Build the famous Pong Arcade Game """

from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
import time

""" Initialise the screen """
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turns off the screen updates

""" Initialise the paddle """

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

""" Initialise the ball """
ball = Ball()


""" Initialise movement keys """
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()
