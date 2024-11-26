import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "Up")

score = Scoreboard()
car_list = []
car = CarManager()
car_list.append(car)
ct = 0
ok = 1

game_is_on = True
while game_is_on:
    if ct % 6 == 0 and ok:
        car = CarManager()
        car_list.append(car)
    time.sleep(0.1)
    screen.update()
    if player.next_level():
        score.update_score()
        ok = 0
        for cars in car_list:
            cars.speed_up()
    for cars in car_list:
        if player.distance(cars) < 20:
            score.game_over()
            game_is_on = False
        if cars.xcor() <= -320:
            cars.goto(x=320, y=randint(-200,200))
        cars.move()
    ct += 1

screen.exitonclick()
