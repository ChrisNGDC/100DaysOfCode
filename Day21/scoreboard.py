import turtle as t

FONT = ("Consolas", 16, "bold")
ALIGN = "center"


class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("#000000")
        self.penup()
        self.setpos(0, 315)
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score}", False, ALIGN, FONT)

    def game_over(self):
        self.color("#FFFFFF")
        self.setpos(0, 100)
        self.write(f"GAME OVER", False, ALIGN, FONT)

    def restart(self):
        self.clear()
        self.__init__()
