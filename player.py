import turtle 
from turtle import Turtle
from scoreboard import Scoreboard
from main import CarSpawner
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
Scoreboard = Scoreboard()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("coral")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        print(self.ycor())
    def Test_Next_Level(self):
        if self.ycor()>FINISH_LINE_Y:  
          return True
    def Death(self,x):
        self.pendown()
        self.write("GAME OVER",font =("Times New Roman",32,"normal"))
      
    def up(self):
      self.forward(MOVE_DISTANCE)
      if self.Test_Next_Level():
        self.goto(STARTING_POSITION)
        Scoreboard.rescore()
        CarSpawner.go += 2
    