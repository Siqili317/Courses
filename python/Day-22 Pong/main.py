"""
1. create the screen
2. create and move a paddle
3. create another paddle
4. create the ball and make it move
5. detect collision with wall and bounce
6. detech collision with paddle
7. detech when paddle misses
8. keep score
"""

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('My Pong Game')
screen.tracer(0)

paddle_right = Paddle((350,0))
paddle_left = Paddle((-350, 0))


screen.listen()
screen.onkey(fun=paddle_left.up, key='w')
screen.onkey(fun=paddle_left.down, key='s')
screen.onkey(fun=paddle_right.up, key='Up')
screen.onkey(fun=paddle_right.down, key='Down')


ball = Ball()
scoreboard =  Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall and bounce
    if ball.collision_with_wall():
        ball.bounce_y()
    
    # Detech collision with paddle and bounce
    if ball.collison_with_paddle(paddle=paddle_right) or ball.collison_with_paddle(paddle=paddle_left):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    
    # Detect R paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    
screen.exitonclick()





