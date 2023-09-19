import math
import turtle as t
import random as r
import colorgram as c

tim = t.Turtle()
tim.speed(0)

screen = t.Screen()
screen.title('Turtle demo')
screen.bgcolor('#FFFFFF')
t.colormode(255)

rgb_colors = []
colors = c.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


def random_color():
    return r.choice(rgb_colors)


def next_dot():
    tim.forward(dot_sep)


def next_line():
    tim.setpos(x_home, tim.ycor() + dot_sep)


def draw_dot():
    tim.dot(radius, random_color())


def draw_line(amount):
    for _ in range(amount):
        draw_dot()
        next_dot()


def draw_lines(lines_amount, dots_amount):
    for _ in range(lines_amount):
        draw_line(dots_amount)
        next_line()


radius = 20
dot_sep = 50
dot_amount = 10
line_amount = 10

tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(318.2)
tim.setheading(0)
x_home = tim.xcor()

draw_lines(line_amount,dot_amount)
screen.mainloop()
