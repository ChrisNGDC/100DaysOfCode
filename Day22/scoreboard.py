import turtle as t


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("#FFFFFF")
        self.hideturtle()
        self.penup()
        self.setpos(0, 290)
        self.write(f'{self.l_score} - {self.r_score}', False, "center", ("Consolas", 26, "bold"))

    def update_score(self):
        self.clear()
        self.write(f'{self.l_score} - {self.r_score}', False, "center", ("Consolas", 26, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def restart(self):
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def end_game(self):
        if self.r_score == 7:
            winner = 'Right'
            pos = 215
        else:
            winner = 'Left'
            pos = -215
        self.setpos(pos, 225)
        self.write(f'{winner} side Wins!', False, "center", ("Consolas", 26, "bold"))
