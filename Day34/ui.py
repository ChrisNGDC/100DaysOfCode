import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = tk.Tk()
        self.window.title('Trivia Quiz')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.scoreboard = tk.Label(text=f'Score: 0/0', bg=self.window.cget('bg'), fg="#FFFFFF",
                                   font=('Consolas', 15, 'bold'))
        self.scoreboard.grid(row=0, column=0, columnspan=2)

        self.canvas = tk.Canvas(bg="#FFFFFF")
        self.canvas.config(width=300, height=250, borderwidth=0, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", fill=self.window.cget('bg'),
                                                     font=('Arial', 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_img = tk.PhotoImage(file='./images/true.png')
        self.true_button = tk.Button(image=self.true_img, highlightthickness=0, relief="flat",
                                     bg=self.window.cget('bg'), command=self.true_pressed)
        self.true_button.grid(row=2, column=0, padx=20)

        self.false_img = tk.PhotoImage(file='./images/false.png')
        self.false_button = tk.Button(image=self.false_img, highlightthickness=0, relief="flat",
                                      bg=self.window.cget('bg'), command=self.false_pressed)
        self.false_button.grid(row=2, column=1, padx=20)

        self.ask_next_question()

        self.window.mainloop()

    def disable_buttons(self):
        self.true_button.config(state='disabled')
        self.false_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_correct: bool):
        self.disable_buttons()
        if is_correct:
            self.canvas.config(bg='#00FF00')
        else:
            self.canvas.config(bg='#FF0000')
        self.scoreboard.config(text=f'Score: {self.quiz.score}/{self.quiz.current_question}')
        self.window.after(1000, self.ask_next_question)

    def ask_next_question(self):
        self.canvas.config(bg='#FFFFFF')
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question().text)
            self.true_button.config(state='normal')
            self.false_button.config(state='normal')
        else:
            self.canvas.itemconfig(self.question_text, text='Congratulations, quiz completed!')
