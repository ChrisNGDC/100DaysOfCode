import turtle as t
import random as r

screen = t.Screen()
screen.setup(500, 400)
screen.bgcolor("#000000")

t.speed(0)
t.hideturtle()
t.pencolor("#FFFFFF")
t.penup()
t.goto(230, 200)
t.pendown()
t.goto(230, -200)

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

turtles = []
y_pos = [110.0, 70.0, 30.0, -10.0, -50.0, -90.0]
for i in range(len(colors)):
    new_turtle = t.Turtle("turtle")
    new_turtle.penup()
    new_turtle.speed(0)
    new_turtle.color(colors[i])
    new_turtle.setpos(-240, y_pos[i])
    turtles.append(new_turtle)

bet = t.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
while bet not in colors:
    bet = t.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

race_over = False
winner_color = "None"
while not race_over:
    for turtle in turtles:
        turtle.forward(r.random() * 10)
        if turtle.xcor() >= 217.8:
            race_over = True
            winner_color = turtle.color()[0]
            break

if winner_color == bet:
    print(f"You've win!! The winning turtle is {winner_color}.")
else:
    print(f"You've lost!! The winning turtle is {winner_color}.")
screen.mainloop()
