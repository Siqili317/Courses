from turtle import Turtle

ALIGN = 'left'
FONT = ('Arial', 30, 'normal')

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.score = 0
        self.color('black')
        self.penup()
        self.goto(-285, 250)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align=ALIGN, font=FONT)
    
    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='Center', font=FONT)
    