from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 24, 'normal')



class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.score = 0
        self.high_score = self.read_high_score()
        self.color('white')
        self.penup()
        self.goto(0, 230)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGN, font=FONT)
    
    def increase_score(self):
        self.score = self.score + 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_high_score(self.high_score)
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
    
    def read_high_score(self):
        with open(r'data.txt', mode='r') as file:
            return int(file.read())
    
    def write_high_score(self, score):
        with open(r'data.txt', mode='w') as file:
            file.write(str(score))

    