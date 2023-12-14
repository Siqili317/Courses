from turtle import Turtle
import random

MOVE_DISTANCE = 10

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


class CarManagement():
    def __init__(self) -> None:
        self.all_cars = [ ]
        self.new_car(x=-100)
        self.new_car(x=40)
        
    
    def new_car(self, x=280):
        car = Turtle(shape='square')
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        car.color(random.choice(colors))
        car.goto(x, random.randint(-280, 280))
        self.all_cars.append(car)

    
    def move(self, speed = 20):
        for car in self.all_cars:
            car.goto(car.xcor() - speed, car.ycor())


    
    
