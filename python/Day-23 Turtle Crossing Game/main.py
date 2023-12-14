from turtle import Turtle, Screen
from player import Player
from car_manager import CarManagement
from scoreboard import Scoreboard
import time
import random

CAR_SPEED = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.title('My Turtle Crossing Game')
screen.tracer(0)

my_player = Player()
scoreboard = Scoreboard()
car_management = CarManagement()

screen.listen()
screen.onkey(my_player.go_up, key="Up")

move_speed = 10
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Control new car generation speed
    if (random.randint(1,8)==1):
        car_management.new_car()
    
    #Move cars
    car_management.move(move_speed)

    #Reach finish line and level up
    if my_player.ycor() > 280:
        my_player.goto(0, -280)
        scoreboard.increase_score()
        move_speed += 10
    
    #Detact collision with tail
    for car in car_management.all_cars:
        if my_player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

    





