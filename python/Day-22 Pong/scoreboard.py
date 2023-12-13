from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 44, 'normal')

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 230)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"{self.l_score}:{self.r_score}", align=ALIGN, font=FONT)
    
    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score +=1
        self.clear()
        self.update_scoreboard()
    