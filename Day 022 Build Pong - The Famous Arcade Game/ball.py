""" Ball Class """
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()  # Call the Turtle class constructor
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # Reverse the y_move direction

    def bounce_x(self):
        self.x_move *= -1  # Reverse the x_move direction
        self.move_speed *= (
            0.9  # Increase the speed of the ball every time it hits a paddle
        )

    def reset_position(self):
        self.goto(0, 0)  # Reset the ball to the center of the screen
        self.move_speed = 0.1  # Reset the speed of the ball
        self.bounce_x()  # Reverse the x_move direction so other player gets first turn
