# CASE 1 Use open
# with open('weather_data.csv', mode='r') as file:
#     weather_data = file.readlines()
#     print(file)

# CASE 2 Use CSV reader
# import csv

# with open('weather_data.csv') as file:
#     weather_data = csv.reader(file)
#     temp = []
#     for row in weather_data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#     print(temp)

# CASE 3 Use Pandas
# import pandas as pd

# weather_data = pd.read_csv('weather_data.csv')
# print(weather_data['temp'].max())

# CASE 4 Use Pandas
# import pandas as pd
# data = pd.read_csv('2018_Central_Park_Squirrel_Census.csv')
# out = data.groupby('Primary Fur Color').size().reset_index(name = 'count')
# out.to_csv('fur_color_summary.csv')

from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

t = Turtle(shape=image)
data = pd.read_csv('50_states.csv')
all_states = data['state'].to_list()
guessed_states = []

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 states guessed', prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data['state']==answer_state]
        point = Turtle(shape='circle')
        point.hideturtle()
        point.penup()
        point.goto(int(state_data.x), int(state_data.y))
        point.write(state_data.state.item())

screen.mainloop()