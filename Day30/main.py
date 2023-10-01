import tkinter as t
import random as r
import pyperclip
import json
import string
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = string.printable[10:62]
numbers = string.printable[:10]
symbols = string.printable[62:94]


def generate_password():
    rand_letters = r.sample(population=letters, k=r.randint(8, 12))
    rand_symbols = r.sample(population=symbols, k=r.randint(4, 6))
    rand_numbers = r.sample(population=numbers, k=r.randint(4, 6))
    rand_chars = rand_letters + rand_symbols + rand_numbers

    r.shuffle(rand_chars)
    created_password = "".join(rand_chars)

    password_entry.delete(0, t.END)
    password_entry.insert(0, created_password)
    pyperclip.copy(created_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    mail = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'Mail': mail,
            'Password': password
        }
    }
    correct_data = True
    if not (website and mail and password):
        messagebox.showwarning(title='Error', message=f'Please fill all entry')
        correct_data = False
    if correct_data and messagebox.askyesno('Confirm data',
                                            f"Is the following correct\nSite: {website}\nMail: {mail}\nPassword: {password}"):
        try:
            with open('./data.json', 'r') as file:
                data = json.load(file)
            if website in data and messagebox.askyesno("Warning",
                                                       f"There is already a password saved for {website}.\nWould you like to overwrite?"):
                data.update(new_data)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            data = new_data
        with open('./data.json', 'w') as file:
            json.dump(data, file, indent=4)
        website_entry.delete(0, t.END)
        password_entry.delete(0, t.END)
        website_entry.focus()


# ---------------------------- SEARCH DATA ------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open('./data.json', 'r') as file:
            data = json.load(file)
        info = data[website]
        messagebox.showinfo(title=f'{website}', message=f"Mail: {info['Mail']}\nPassword: {info['Password']}")
        pyperclip.copy(info['Password'])
    except KeyError:
        messagebox.showerror(title='Error', message=f'Website {website} is not saved.')
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        messagebox.showerror(title='Error', message=f'There are no passwords saved.')


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
website_entry.grid(column=1, row=1, sticky='NSEW', pady=1, padx=1)
website_entry.focus()

website_search_button = t.Button(text='Search', font=('Consolas', 10, 'normal'), relief='solid',
                                 bg=window.cget('bg'), borderwidth=.5, command=search)
website_search_button.grid(column=2, row=1, sticky='EW', pady=1, padx=1)

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
