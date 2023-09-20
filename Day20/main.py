import turtle as t
import time
from snake import Snake

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("#000000")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_over = False
while not game_over:
    screen.update()
    snake.update()
    screen.update()
    time.sleep(snake.difficulty)


screen.mainloop()
