import random as r
import turtle as t

APPLE_SIZE_FACTOR = .5  # Only one to change


class Apple(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#FF0000")
        self.shapesize(APPLE_SIZE_FACTOR, APPLE_SIZE_FACTOR, 0)
        self.speed(0)
        self.move()

    def move(self):
        self.setpos(r.randrange(-300, 300, 20), r.randrange(-300, 300, 20))

    def restart(self):
        self.__init__()
