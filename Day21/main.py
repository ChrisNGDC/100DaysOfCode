import turtle as t
import time
from snake import Snake
from apple import Apple
from scoreboard import ScoreBoard

screen = t.Screen()
screen.setup(700, 700)
screen.bgcolor("#CCCCCC")
screen.title("Snake")
screen.tracer(0)

bg = t.Turtle("square")
bg.fillcolor("#000000")
bg.resizemode("user")
bg.shapesize(31, 31, 0)

snake = Snake()
apple = Apple()
score = ScoreBoard()

play = "yes"
while play == "yes":

    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")
    screen.onkeypress(lambda: print(f'Snake: {snake.head.pos()}\nApple: {apple.pos()}'), "space")

    game_over = False
    while not game_over:
        screen.update()
        time.sleep(snake.difficulty)
        snake.update()
        if snake.head.distance(apple) < 10:
            score.increase_score()
            apple.move()
            snake.up_difficulty()
            snake.extend()
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            score.game_over()
            game_over = True
        for part in snake.body[1:]:
            if snake.head.distance(part) < 10:
                score.game_over()
                game_over = True
                break
    play = t.textinput("Play Again?", "Do you want to play again? Type 'yes' or 'no")
    while play is None or play.lower() not in ["yes", "no"]:
        play = t.textinput("Play Again?", "Do you want to play again? Type 'yes' or 'no").lower()
    if play == "yes":
        snake.restart()
        apple.restart()
        score.restart()

screen.bye()
screen.mainloop()
