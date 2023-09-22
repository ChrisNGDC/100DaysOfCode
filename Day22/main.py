import turtle as t
import time
from table import create_table
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(850, 700)
screen.bgcolor("#000000")
screen.title("Pong")
screen.tracer(0)

create_table()

r_paddle = Paddle((370, -25))
l_paddle = Paddle((-370, -25))
ball = Ball()
scoreboard = Scoreboard()
elements = [r_paddle, l_paddle, ball, scoreboard]

play = "yes"
while play == "yes":

    screen.listen()
    screen.onkeypress(r_paddle.up, "Up")
    screen.onkeypress(r_paddle.down, "Down")
    screen.onkeypress(l_paddle.up, "w")
    screen.onkeypress(l_paddle.down, "s")

    game_over = False
    while not game_over:
        time.sleep(.01)
        screen.update()
        ball.move()

        if ball.ycor() < -315 or ball.ycor() > 265:
            ball.wall_bounce()
        if (355 > ball.xcor() > 350 and r_paddle.distance(ball) <= 58) or (-355 < ball.xcor() < -350 and l_paddle.distance(ball) <= 58):
            ball.paddle_bounce()
        if ball.xcor() > 380:
            ball.restart()
            scoreboard.l_point()
        if ball.xcor() < -380:
            ball.restart()
            scoreboard.r_point()
        if scoreboard.l_score == 7 or scoreboard.r_score == 7:
            scoreboard.end_game()
            game_over = True
    play = t.textinput("Play Again?", "Do you want to play again? Type 'yes' or 'no")
    while play is None or play.lower() not in ["yes", "no"]:
        play = t.textinput("Play Again?", "Do you want to play again? Type 'yes' or 'no").lower()
    if play == "yes":
        for elem in elements:
            elem.restart()

screen.bye()
screen.mainloop()
