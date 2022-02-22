
import time
from turtle import Turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import scoreboard

Player = Player()
print(scoreboard.Scoreboard)
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
ListOfObjects = []

CarSpawner = CarManager(ListOfObjects)

game_is_on = True
i = 0
screen.listen()
while game_is_on:
    i+=1
    time.sleep(0.1)
    if i%6==0:
        ListOfObjects.append(CarSpawner.carAdd())
    CarSpawner.move()
    screen.onkey(fun=Player.up,key="space")
    if CarSpawner.contact(Player) ==True:
        Player.Death(game_is_on)
        game_is_on=False
    screen.update()
