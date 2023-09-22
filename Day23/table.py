import turtle as t


def make_line(controller, pos1, pos2):
    controller.penup()
    controller.setpos(pos1)
    controller.pendown()
    controller.goto(pos2)


def make_rectangle(controller, init_pos, width, height):
    controller.penup()
    controller.setpos(init_pos)
    controller.pendown()
    for _ in range(4):
        controller.setheading(0)
        controller.forward(width)
        controller.setheading(270)
        controller.forward(height)
        controller.setheading(180)
        controller.forward(width)
        controller.setheading(90)
        controller.forward(height)


def create_table():
    line = t.Turtle()
    line.hideturtle()
    line.speed(0)
    line.pencolor("#FFFFFF")

    line.pensize(1)
    make_rectangle(line, (-400, 270), 800, 595)
    make_line(line, (-400, 235), (400, 235))
    make_line(line, (-400, -290), (400, -290))

    y = -290
    while y < 245:
        line.penup()
        y += 35
        line.goto(-395, y)
        line.setheading(0)
        while line.xcor() < 400:
            line.pendown()
            line.forward(20)
            line.penup()
            line.forward(15)
