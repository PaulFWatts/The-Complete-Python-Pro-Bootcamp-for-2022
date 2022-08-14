""" Snake Game using OOP"""
import time
from turtle import Screen, Turtle

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen updates (animations)

snake = Snake()  # Create the snake object

""" Define use of arrow keys to control the snake """
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Pause the game for 0.1 seconds
    snake.move()  # Move the snake


screen.exitonclick()
