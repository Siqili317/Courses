from turtle import Turtle, Screen
import random
import colorgram
# import turtle
# import turtle as t


timmy = Turtle()
timmy.shape('turtle')
timmy.color('green', 'red')

# Draw different shapes with random color

"""for i in range(4, 11):
    turn_angle = 360/i
    tup = (random.random(),random.random(),random.random() )
    timmy.pencolor(tup)
    for j in range(i):
        timmy.forward(100)
        timmy.right(turn_angle)"""


# Draw a random walk

"""keep_going = 200
timmy.speed(8)
timmy.pensize(15)

while keep_going>0:
    turn_angle = random.randint(0,3)*90
    tup = (random.random(),random.random(),random.random() )
    timmy.pencolor(tup)
    timmy.setheading(turn_angle)
    timmy.forward(30)
    keep_going -=1"""


#Make a Spirograph
"""rep = 90
while rep > 0:
    tup = (random.random(),random.random(),random.random() )
    timmy.pencolor(tup)
    timmy.circle(50)
    timmy.right(4)
    rep -=1"""

colors = colorgram.extract('c.png', 30)
rgb_color = []
for color in colors:
    rgb_color.append((color.rgb.r, color.rgb.g, color.rgb.b))

screen = Screen()
screen.colormode(255)
timmy.home()
timmy.hideturtle()

row = 10
while row > 0:

    col = 10
    while col > 0:
        timmy.dot(20, random.choice(rgb_color))
        timmy.up()
        timmy.forward(50)
        timmy.down()
        col -=1
    timmy.up()
    timmy.setpos(timmy.xcor() - 500, timmy.ycor() + 50)
    timmy.down()



screen.exitonclick()