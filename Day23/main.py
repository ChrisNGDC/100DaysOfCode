import turtle as t
import time
from table import create_table
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(800, 665)
screen.bgcolor("#000000")
screen.title("Frogger")
screen.tracer(0)

create_table()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

play = "yes"
while play == "yes":

    screen.listen()
    screen.onkeypress(player.move_up, "w")
    screen.onkeypress(player.move_down, "s")
    screen.onkeypress(player.move_left, "a")
    screen.onkeypress(player.move_right, "d")

    game_over = False
    while not game_over:
        time.sleep(.01)
        screen.update()
        scoreboard.update_score()
        car_manager.create_car()
        car_manager.move_cars()
        cars = len(car_manager.cars)
        reserve = len(car_manager.reserve)
        print(f'Cars: {cars} - Reserve: {reserve} - Total: {cars + reserve}')
        if player.ycor() >= 240:
            screen.update()
            time.sleep(.5)
            scoreboard.level += 1
            player.restart()
            car_manager.increase_difficulty()
        for car in car_manager.cars:
            if player.distance(car) < 25:
                game_over = True
                scoreboard.end_game()

    play = t.textinput("Play Again?", "Do you want to play again? Type 'yes' or 'no")
    while play is None or play.lower() not in ["yes", "no"]:
        play = t.textinput("Play Again?", "Do you want to play again? Type 'yes' or 'no").lower()
    if play == "yes":
        car_manager.restart()
        player.restart()
        scoreboard.restart()

screen.bye()
screen.mainloop()
