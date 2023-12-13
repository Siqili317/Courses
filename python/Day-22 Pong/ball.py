from turtle import Turtle




class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setheading(45)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    def reset_position(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1
    
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def collision_with_wall(self):
        return abs(self.ycor())>280
    
    def collison_with_paddle(self, paddle):
        if self.distance(paddle) < 50 and abs(self.xcor()) > 320:
            return True
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):        
        self.y_move *= -1
