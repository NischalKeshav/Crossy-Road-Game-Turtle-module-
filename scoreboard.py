from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def  __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto (-300,200)
        self.pendown()
        self.level = 1
        self.x = f"Level: {self.level}  "
        self.write(self.x,font = FONT)
    def rescore(self):
        self.clear()
        self.level+=1
        self.pendown()
        self.x =  f"Level: {self.level}  "
        self.write(self.x,font = FONT)
        print(self.level)
        self.write(self.x,font = FONT)
