import turtle as t


def create_table():
    line = t.Turtle()
    line.hideturtle()
    line.speed(0)
    line.pencolor("#FFFFFF")

    line.pensize(1)
    line.penup()
    line.setpos(-400, 275)
    line.pendown()
    line.goto(400, 275)
    line.goto(400, -325)
    line.goto(-400, -325)
    line.goto(-400, 275)

    line.pensize(5)
    line.penup()
    line.goto(0, 265)
    line.setheading(270)
    while line.ycor() > -325:
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(15)
