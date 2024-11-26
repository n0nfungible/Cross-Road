FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x = -280, y = 260)
        self.write(f"LEVEL: {self.score}", font = FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {self.score}", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER!", font = FONT, align= "center")
