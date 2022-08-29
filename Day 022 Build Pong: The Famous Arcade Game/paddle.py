""" Paddle Class"""

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):  # position is a tuple
        super().__init__()  # Initialise the Turtle class
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        """Move the paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Move the paddle down"""
        new_x = self.ycor() - 20
        self.goto(self.xcor(), new_x)
