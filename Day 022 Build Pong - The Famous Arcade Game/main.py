""" Build the famous Pong Arcade Game """

import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

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

""" Initialise the scoreboard """
scoreboard = Scoreboard()


""" Initialise movement keys """
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


""" Main game loop """
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if (
        scoreboard.l_score == 5 or scoreboard.r_score == 5
    ):  # Check if either player has scored 5 points
        scoreboard.game_over()
        game_is_on = False  # Game is over

    # Check for a collision with the top or bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check for a collision with the paddles
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect when right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
