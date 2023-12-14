from turtle import Turtle

PADDLE_LEFT_X = -350
STARTING_POSITIONS = [(PADDLE_LEFT_X, 0), (PADDLE_LEFT_X, 20), (PADDLE_LEFT_X, 40), (PADDLE_LEFT_X, -20), (PADDLE_LEFT_X, -40)]
MOVE_SIZE = 20

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.paddle = self.create_paddle(position)

    def create_paddle(self, position):
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_SIZE)
    
    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_SIZE)
