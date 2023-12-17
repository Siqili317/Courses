from tkinter import *

window = Tk()
window.title('Mile to Km Convertor')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
input = Entry(width=10)
input.grid(column=1,row=0)

# Label
miles_label = Label(text='Miles', font=('Arial', 14))
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=('Arial', 14))
is_equal_to_label.grid(column=0, row=1)

km_value_label = Label(text="", font=('Arial', 14))
km_value_label.grid(column=1, row=1)

km_unit_label = Label(text="Km", font=('Arial', 14))
km_unit_label.grid(column=2, row=1)


# Button
def click_button():
    value_in_miles = input.get()
    value_in_km = float(value_in_miles) * 1.609
    km_value_label.config(text=value_in_km)

my_button = Button(text='Calculate', command=click_button)
my_button.grid(column=1, row=2)

# Text
# Spinbox
# Scale
# Checkbox
#Radiobutton
#Listbox

window.mainloop()