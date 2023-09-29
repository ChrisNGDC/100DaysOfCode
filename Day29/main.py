import tkinter as t
import random as r
import pandas as p
import pyperclip
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'tim', 'u',
           'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    rand_letters = r.choices(population=letters, k=r.randint(8, 10))
    rand_symbols = r.choices(population=symbols, k=r.randint(2, 4))
    rand_numbers = r.choices(population=numbers, k=r.randint(2, 4))
    rand_chars = rand_letters + rand_symbols + rand_numbers

    r.shuffle(rand_chars)
    created_password = "".join(rand_chars)

    password_entry.delete(0, t.END)
    password_entry.insert(0, created_password)
    pyperclip.copy(created_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data = {
        'Website': [website_entry.get()],
        'Mail': [email_user_entry.get()],
        'Password': [password_entry.get()]
    }
    correct_data = True
    for info in data:
        if data[info] == [""]:
            messagebox.showwarning(title='Error', message=f'{info} missing')
            correct_data = False
    if correct_data and messagebox.askokcancel(title='Confirm data',
                                               message=f"Is the following correct\nSite: {data['Website'][0]}\nMail: {data['Mail'][0]}\nPassword: {data['Password'][0]}"):
        df = p.DataFrame(data)
        df.to_csv('data.csv', mode='a', index=False, header=False)
        website_entry.delete(0, t.END)
        password_entry.delete(0, t.END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = t.Tk()
window.title('Password Manager')
window.config(pady=50, padx=50, bg="#FFFFFF")

canvas = t.Canvas(width=200, height=200, bg=window.cget('bg'), highlightthickness=0)
logo_img = t.PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = t.Label(text='Website:', anchor='e', bg=window.cget('bg'))
website_label.grid(column=0, row=1, sticky='NSEW')

website_entry = t.Entry(relief='solid', borderwidth=.5, bg=window.cget('bg'))
website_entry.grid(column=1, row=1, columnspan=2, sticky='NSEW', pady=1, padx=1)
website_entry.focus()

email_user_label = t.Label(text='Email/Username:', anchor='e', bg=window.cget('bg'))
email_user_label.grid(column=0, row=2, sticky='NSEW')

email_user_entry = t.Entry(relief='solid', borderwidth=.5, bg=window.cget('bg'))
email_user_entry.insert(0, "chrisgabor95@gmail.com")
email_user_entry.grid(column=1, row=2, columnspan=2, sticky='NSEW', pady=1, padx=1)

password_label = t.Label(text='Password:', anchor='e', bg=window.cget('bg'))
password_label.grid(column=0, row=3, sticky='NSEW')

password_entry = t.Entry(relief='solid', borderwidth=.5, bg=window.cget('bg'))
password_entry.grid(column=1, row=3, sticky='NSEW', pady=1, padx=1)

generate_password_button = t.Button(text='Generate', font=('Consolas', 10, 'normal'), relief='solid',
                                    bg=window.cget('bg'), borderwidth=.5, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky='EW', pady=1, padx=1)

add_password_button = t.Button(text='Add', font=('Consolas', 10, 'normal'), relief='solid', bg=window.cget('bg'),
                               borderwidth=.5, command=save)
add_password_button.grid(column=1, row=4, columnspan=2, sticky='EW', pady=1, padx=1)

window.mainloop()
