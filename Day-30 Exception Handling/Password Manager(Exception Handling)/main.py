# ===== Welcome back to the upgraded version of my beautiful mini application of Day-29 ===== #
# In this version I have used Json file instead of txt file to store the data in a systematic way.
# Also used exception handling to showcase errors well.

import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # List Comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)  # Join method

    password_entry.insert(0, password)
    pyperclip.copy(password)  # It copies the generated password into your clipboard so that you can paste it anywhere


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()  # Get the data which is entered in the website text field
    email = email_entry.get()
    password_field = password_entry.get()
    new_data = {
        website.title(): {
            "email": email,
            "password": password_field
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password_field) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # If data.json file doesn't exist, below file handling is used
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter website to search the data.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # here type of data variable is dictionary
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="File not found. Generate one by adding data.")
        else:
            if website in data:
                # How to fetch data from dictionary inside dictionary?
                email = data[website]["email"]  # data is itself a dictionary and website name is another dictionary
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Oops", message="Data doesn't exist in the file.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)  # Canvas width and height should be double than image co-ordinates given below
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()  # To show cursor
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "garv@gmail.com")  # To already show your email
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(row=1, column=2)
window.mainloop()
