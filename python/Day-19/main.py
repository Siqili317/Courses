from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title = 'Make your bet', prompt='Which turtle will win the race? enter a color:')

turtles = []
for t in range(6):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[t])
    turtle.penup()
    turtle.goto(x=-238, y=-100 + 40*t)
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() < 230:
            turtle.forward(random.randint(0, 10))
        else:
            is_race_on = False
            winner = turtle.pencolor()

if winner == user_bet:
    print("You win!")
else:
    print(f"You bet for {user_bet}, but the winner is {winner}")


def move_forwards():
    turtle.forward(10)
def move_backwards():
    turtle.backward(10)
def turn_left():
    turtle.left(10)
def turn_right():
    turtle.right(10)
def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(fun=move_forwards, key='d')
screen.onkey(fun=move_backwards, key='a')
screen.onkey(fun=turn_right, key='s')
screen.onkey(fun=turn_left, key='w')
screen.onkey(fun=clear, key='c')
screen.exitonclick()