import turtle as t

PADDLE_SPEED = 25


class Paddle(t.Turtle):
    def __init__(self, init_pos):
        super().__init__("square")
        self.resizemode("user")
        self.shapesize(5, 1)
        self.speed(0)
        self.color("#FFFFFF")
        self.penup()
        self.init_pos = init_pos
        self.restart()

    def up(self):
        if self.ycor() < 225:
            self.goto(self.xcor(), self.ycor() + PADDLE_SPEED)

    def down(self):
        if self.ycor() > -275:
            self.goto(self.xcor(), self.ycor() - PADDLE_SPEED)

    def restart(self):
        self.setpos(self.init_pos)
