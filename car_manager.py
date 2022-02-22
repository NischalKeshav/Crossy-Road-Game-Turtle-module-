from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self,lev=1):
        self.ListOfCars =[] 
        self.level= lev
    def carAdd(self):
        car = Turtle()  
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_len=2)
        car.goto(300,random.randrange(-200,250))
        car.right(0)
        car.go = 8
        self.ListOfCars.append(car)
                  
    def move(self):
        for i in self.ListOfCars:
            i.backward(i.go)
            if i.xcor()<-320:
                self.ListOfCars.remove(i)
    def contact(self,x):
        for car in self.ListOfCars:
            if car.distance(x)<30:
              return True
            else:
              continue