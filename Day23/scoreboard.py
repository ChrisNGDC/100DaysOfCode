import turtle as t


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("#FFFFFF")
        self.hideturtle()
        self.penup()
        self.setpos(-380, 280)
        self.write(f'LEVEL {self.level}', False, "left", ("Consolas", 26, "bold"))

    def update_score(self):
        self.clear()
        self.write(f'LEVEL {self.level}', False, "left", ("Consolas", 26, "bold"))

    def restart(self):
        self.clear()
        self.__init__()

    def end_game(self):
        self.setpos(380, 280)
        self.write(f'GAME OVER', False, "right", ("Consolas", 26, "bold"))
