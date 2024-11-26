from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1 ,stretch_len= 2)
        self.color(f"{choice(COLORS)}")
        self.goto(x=320, y=randint(-200,200))
        self.setheading(180)
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        if self.xcor() > -320:
            self.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
