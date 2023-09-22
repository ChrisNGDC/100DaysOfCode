import turtle as t

FONT = ("Consolas", 16, "bold")


class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'rt') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("#000000")
        self.penup()
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.color("#000000")
        self.setpos(-300, 315)
        self.write(f"SCORE : {self.score}", False, "left", FONT)
        self.setpos(300, 315)
        self.write(f"HIGH SCORE : {self.high_score}", False, "right", FONT)

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'wt') as data:
                data.write(str(self.high_score))
        self.update_score()

    def game_over(self):
        self.update_high_score()
        self.color("#FFFFFF")
        self.setpos(0, 100)
        self.write(f"GAME OVER", False, "center", FONT)

    def restart(self):
        self.clear()
        self.score = 0
        self.update_score()
