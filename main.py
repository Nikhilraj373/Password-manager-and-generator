from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    pass_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    pass_num = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = pass_num + pass_symbols + pass_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_save = website_entry.get()
    email_save = email_entry.get()
    password_save = password_entry.get()

    if len(website_save) == 0 or len(password_save) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure not to leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website_save, message=f"Details entered: \nEmail/username: {email_save}\n"
                                                                   f"Password: {password_save}\n is it ok save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_save} | {email_save} | {password_save}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

#Labels
website = Label(text="Website:")
website.grid(column=0, row=1)
email = Label(text="Email/Username:")
email.grid(column=0, row=2)
password = Label(text="Password")
password.grid(column=0, row=3)

#Entries
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "nikhilraj373@gmail.com")
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

#buttons
generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(column=2, row=3)
add = Button(text="Add", width=44, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()