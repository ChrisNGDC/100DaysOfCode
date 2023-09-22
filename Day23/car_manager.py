import turtle as t
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1.1
TRACKS_Y = [-272.5, -237.5, -202.5, -167.5, -132.5, -97.5, -62.5, -27.5, 7.5, 42.5, 77.5, 112.5, 147.5, 182.5, 217.5]


class CarManager:
    def __init__(self):
        self.cars = []
        self.reserve = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if r.randint(1, 10) == 1:
            if self.reserve:
                new_car = self.reserve.pop()
            else:
                new_car = t.Turtle("square")
            new_car.resizemode("user")
            new_car.shapesize(1.25, 2, 0)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(r.choice(COLORS))
            new_y = r.choice(TRACKS_Y)
            new_x = 385
            if self.cars:
                if self.cars[-1].xcor() > 335 and self.cars[-1].ycor() == new_y:
                    new_x = self.cars[-1].xcor() + 50
            new_car.setpos(new_x, new_y)
            self.cars.append(new_car)

    def reserve_car(self, car):
        car.goto(500, 0)
        self.reserve.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.cars_speed)
            if car.xcor() < -375:
                self.cars.remove(car)
                self.reserve_car(car)

    def increase_difficulty(self):
        self.cars_speed += MOVE_INCREMENT

    def restart(self):
        for car in self.cars:
            car.reset()
            car.penup()
            car.hideturtle()
        self.__init__()
