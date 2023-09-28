import math
import tkinter as t

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
reps = 0
timer = "None"

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    if timer != "None":
        window.after_cancel(timer)
    global reps
    reps = 0
    check.config(text="")
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(timer_shadow, text="00:00")
    start_button.config(state="normal")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    start_button.config(state="disabled")
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps in [1, 3, 5, 7]:
        title.config(text="Work", fg=GREEN)
        countdown(work_sec)
    elif reps in [2, 4, 6]:
        title.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    elif reps == 8:
        title.config(text="Break", fg=RED)
        countdown(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    minutes = count // 60
    sec = count % 60
    canvas.itemconfig(timer_text, text=f'{minutes:02d}:{sec:02d}')
    canvas.itemconfig(timer_shadow, text=f'{minutes:02d}:{sec:02d}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        check.config(text='✔' * math.ceil(reps / 2), fg=GREEN)  # u'\u2713'
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = t.Tk()
window.title("Pomodoro")
window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
window.config(bg=YELLOW, padx=50, pady=50)

title = t.Label(text="Timer", font=(FONT_NAME, 50, "normal"), bg=window.cget("bg"), fg=GREEN)
title.grid(column=1, row=0)

canvas = t.Canvas(width=200, height=224, bg=window.cget("bg"), highlightthickness=0)

tomato = t.PhotoImage(file='./tomato.png')

canvas.create_image(100, 112, image=tomato)
canvas.grid(column=1, row=1)

timer_text = canvas.create_text(101, 130, text="00:00", fill="#000000", font=(FONT_NAME, 35, "bold"))
timer_shadow = canvas.create_text(100, 130, text="00:00", fill="#FFFFFF", font=(FONT_NAME, 35, "bold"))

check = t.Label(text='', bg=window.cget("bg"), font=(FONT_NAME, 15, "normal"), justify="center")
check.grid(column=1, row=3)

start_button = t.Button(text='Start', font=(FONT_NAME, 15, "normal"), cursor='hand2', relief='raised', border=2,
                        bg="#FFFFFF",
                        width=5, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = t.Button(text='Reset', font=(FONT_NAME, 15, "normal"), cursor='hand2', relief='raised', border=2,
                        bg="#FFFFFF",
                        width=5, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
