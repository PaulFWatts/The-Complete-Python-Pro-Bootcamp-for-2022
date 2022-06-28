# Goto https://reeborg.ca/reeborg.html to use Karel
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for x in range(1, 7):
    move()
    jump()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
