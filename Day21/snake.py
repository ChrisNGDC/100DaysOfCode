import turtle as t

INITIAL_POS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_SIZE_FACTOR = 1  # Only one to change
SNAKE_SIZE = 20 * SNAKE_SIZE_FACTOR
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.difficulty = .075
        self.direction_locked = False

    def create_snake(self):
        for pos in INITIAL_POS:
            self.add_body_part(pos)

    def add_body_part(self, pos):
        new_turtle = t.Turtle("square")
        new_turtle.resizemode("user")
        new_turtle.shapesize(SNAKE_SIZE_FACTOR, SNAKE_SIZE_FACTOR, 0)
        new_turtle.penup()
        new_turtle.speed(0)
        new_turtle.color("#00FF00")
        new_turtle.setpos(pos)
        self.body.append(new_turtle)

    def extend(self):
        self.add_body_part(self.body[-1].pos())

    def update(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].pos())
        self.head.forward(SNAKE_SIZE)
        self.direction_locked = False

    def up(self):
        if self.head.heading() != DOWN and not self.direction_locked:
            self.head.setheading(UP)
            self.direction_locked = True

    def down(self):
        if self.head.heading() != UP and not self.direction_locked:
            self.head.setheading(DOWN)
            self.direction_locked = True

    def left(self):
        if self.head.heading() != RIGHT and not self.direction_locked:
            self.head.setheading(LEFT)
            self.direction_locked = True

    def right(self):
        if self.head.heading() != LEFT and not self.direction_locked:
            self.head.setheading(RIGHT)
            self.direction_locked = True

    def up_difficulty(self):
        self.difficulty -= .001

    def restart(self):
        for part in self.body:
            part.reset()
        self.__init__()
