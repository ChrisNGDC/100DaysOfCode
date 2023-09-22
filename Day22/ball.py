import turtle as t
import random as r

BALL_INIT_SPEED = 2


class Ball(t.Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("#FFFFFF")
        self.penup()
        self.speed(1)
        self.setpos(0, -25)
        self.ball_speed = BALL_INIT_SPEED
        self.direction = r.choice([r.randint(1,36), r.randint(144,216)])

    def move(self):
        self.setheading(self.direction)
        self.forward(self.ball_speed)

    def wall_bounce(self):
        self.direction = 360 - self.direction

    def paddle_bounce(self):
        if 0 <= self.direction <= 180:
            self.direction = 180 - self.direction
        elif 180 < self.direction < 360:
            self.direction = 540 - self.direction
        self.ball_speed *= 1.1

    def restart(self):
        self.reset()
        self.__init__()
