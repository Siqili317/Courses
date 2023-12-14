from turtle import Turtle

MOVE_STEP = 10

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0, -280)
    
    def go_up(self):
        self.goto(0, self.ycor() + MOVE_STEP)