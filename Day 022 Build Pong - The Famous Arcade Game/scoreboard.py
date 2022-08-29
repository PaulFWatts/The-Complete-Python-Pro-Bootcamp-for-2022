""" Scoreboard Class"""

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Call the Turtle class constructor
        self.hideturtle()
        # self.speed(0)
        self.penup()
        self.color("white")
        self.l_score = 0  # Left player score
        self.r_score = 0  # Right player score
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # Clear the scoreboard to prevent overwriting previous scores
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def update_score(self, player):
        self.clear()
        self.write(
            "Player A: {} Player B: {}".format(player.score_a, player.score_b),
            align="center",
            font=("Courier", 24, "normal"),
        )

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))
