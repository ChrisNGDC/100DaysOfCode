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
        self.difficulty = .1

    def create_snake(self):
        for i in range(3):
            new_turtle = t.Turtle("square")
            new_turtle.resizemode("user")
            new_turtle.shapesize(SNAKE_SIZE_FACTOR, SNAKE_SIZE_FACTOR, 0)
            new_turtle.penup()
            new_turtle.speed(0)
            new_turtle.color("#FFFFFF")
            new_turtle.setpos(INITIAL_POS[i])
            self.body.append(new_turtle)

    def update(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].pos())
        self.head.forward(SNAKE_SIZE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up_difficulty(self):
        self.difficulty -= .001
