# Imports #
import tkinter as t
import pandas as p
import random as r

# Constants and Globals #
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}


# Flip card #
def next_card():
    global flip, current_word
    window.after_cancel(flip)
    current_word = r.choice(data_list_dict)
    canvas.itemconfig(card, image=front_image)
    canvas.itemconfig(language, text='English', fill="#000000")
    canvas.itemconfig(word, text=current_word['English'], fill="#000000")
    flip = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card, image=back_image)
    canvas.itemconfig(language, text='Spanish', fill="#FFFFFF")
    canvas.itemconfig(word, text=current_word['Spanish'], fill="#FFFFFF")


def already_known():
    data_list_dict.remove(current_word)
    save_data()
    next_card()


# Data #

def save_data():
    words_to_learn = p.DataFrame(data_list_dict)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)


try:
    data = p.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data = p.read_csv('./data/Words.csv')
data_list_dict = data.to_dict(orient='records')

# UI #
window = t.Tk()
window.minsize(width=900, height=600)
window.title('Learn English with flash cards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

front_image = t.PhotoImage(file="./images/card_front.png")
back_image = t.PhotoImage(file="./images/card_back.png")
canvas = t.Canvas(width=800, height=526, bg=window.cget('bg'), highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card = canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 150, text="Language", fill="#000000", font=('Ariel', 40, "italic"))
word = canvas.create_text(400, 263, text='word', fill="#000000", font=('Ariel', 60, "bold"))

wrong_image = t.PhotoImage(file="./images/wrong.png")
wrong_button = t.Button(image=wrong_image, highlightthickness=0, relief="flat", bg=window.cget('bg'), command=next_card)
wrong_button.grid(row=1, column=0)

right_image = t.PhotoImage(file="./images/right.png")
right_button = t.Button(image=right_image, highlightthickness=0, relief="flat", bg=window.cget('bg'),
                        command=already_known)
right_button.grid(row=1, column=1)

flip = window.after(3000, func=flip_card)
next_card()

window.mainloop()
