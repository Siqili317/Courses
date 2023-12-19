from tkinter import *
import random
import pandas

timer = None
current_card = {}
#------------------------Display card----------------------------
try:
    file = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    file = pandas.read_csv('data/french_words.csv')
    file.to_csv('data/words_to_learn.csv', index=False)
finally:
    data = file.to_dict(orient='records')

def generate_random_word():
    global current_card
    current_card = random.choice(data)
    canvas.itemconfig(canvas_image, image = card_front_png)
    canvas.itemconfig(card_title, text = 'French', fill = 'black')
    canvas.itemconfig(french_text, text = current_card['French'], fill = 'black')
    count_down()
    
#------------------------Flip card----------------------------
def flip_card():
    canvas.itemconfig(canvas_image, image = card_back_png)
    canvas.itemconfig(card_title, text = 'English', fill = 'white')
    canvas.itemconfig(french_text, text = current_card['English'], fill = 'white')
    global timer
    window.after_cancel(timer)

def count_down():
    global timer
    timer = window.after(3000, func=flip_card)
#------------------------Progress tracker----------------------------
def known_word():
    data.remove(current_card)
    df = pandas.DataFrame(data)
    df.to_csv('data/words_to_learn.csv', index=False)    
    generate_random_word()
    

#------------------------UI----------------------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
card_front_png = PhotoImage(file='images/card_front.png')
card_back_png = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image( 400, 263, image = card_front_png)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
french_text = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

right_png = PhotoImage(file='images/right.png')
wrong_png = PhotoImage(file='images/wrong.png')
right_button = Button(image=right_png, highlightthickness=0, command=known_word).grid(column=1, row=1)
wrong_button = Button(image=wrong_png, highlightthickness=0, command=generate_random_word).grid(column=0, row=1)

generate_random_word()

window.mainloop()

