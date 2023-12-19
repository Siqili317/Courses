from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    selected_letters = [choice(letters) for char in range(randint(8, 10))]
    selected_symbols = [choice(symbols) for char in range(randint(2, 4))]
    selected_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = selected_letters + selected_numbers + selected_symbols
    shuffle(password_list)
    password = ''.join(password_list)

    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email_username,
            'password': password
        }
    }
    if (len(website)==0) or (len(password)==0):
        messagebox.showwarning(message="Please do not leave any field empty!")
    else:
        try:
            with open('data.json', mode='r') as file:
                # 1. Reading old data
                data = json.load(file)
        except FileNotFoundError:
             with open('data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
             # 2. Updating old data with new data
            data.update(new_data)
            with open('data.json', mode='w') as file:
                # 3. Saving new data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(message=f"No data file found.")
    else:
        if website in data:
            password = data[website]['password']
            email = data[website]['email']
            messagebox.showinfo(message=f"Login for {website} is:\n Email:{email}\n Password: {password}")
        else:
            messagebox.showinfo(message=f"No details for {website}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image = logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)
password_label = Label(text = 'Password:')
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
website_entry.focus() # init cursor here
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky=W)
email_username_entry.insert(END, 'myEmail@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky=W)

#Buttons
search_button = Button(text='Search', command=search_password).grid(column=2, row=1)
generate_password_button = Button(text='Generate Password', width=11, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky=W)
add_button = Button(width=32, text='Add', command=add_data)
add_button.grid(column=1, columnspan=2, row=4, sticky=W)

window.mainloop()