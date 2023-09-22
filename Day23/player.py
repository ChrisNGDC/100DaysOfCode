import turtle as t

PLAYER_SPEED = 35
INIT_POS = (0, -312.5)


class Player(t.Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.color("#00FF00")
        self.resizemode("user")
        self.shapesize(1.25, 1.25, 0)
        self.speed(0)
        self.setheading(90)
        self.penup()
        self.setpos(INIT_POS)

    def move_up(self):
        if self.ycor() < 240:
            self.forward(PLAYER_SPEED)

    def move_down(self):
        if self.ycor() > -295:
            self.backward(PLAYER_SPEED)

    def move_left(self):
        if self.xcor() > -385:
            self.setheading(180)
            self.forward(PLAYER_SPEED)
            self.setheading(90)

    def move_right(self):
        if self.xcor() < 385:
            self.setheading(0)
            self.forward(PLAYER_SPEED)
            self.setheading(90)

    def restart(self):
        self.setheading(90)
        self.setpos(INIT_POS)
