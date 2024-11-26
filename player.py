STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")

    def move(self):
        y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def next_level(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False
