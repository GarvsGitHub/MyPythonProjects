# Tiny project for tkinter UI
from tkinter import *


def calculate():
    miles = float(input_text.get())  # Converting string to float
    km = miles * 1.60934
    label3["text"] = f'{km:.2f}'  # To print maximum 2 places after decimal
    # label3.config(text=f'{km:.2f}')


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=55, pady=20)

input_text = Entry(width=10)
input_text.grid(row=0, column=1)
input_text.focus()  # To add curser on the Entry text

label1 = Label(text="Miles", font=("Arial", 10))
label1.grid(row=0, column=2)

label2 = Label(text="is equal to", font=("Arial", 10))
label2.grid(row=1, column=0)

label3 = Label(text="0", font=("Arial", 10))
label3.grid(row=1, column=1)

label4 = Label(text="Km", font=("Arial", 10))
label4.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()  # Holds tkinter window till we close
