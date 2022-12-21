import turtle
from turtle import Turtle
import random

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_y():
    car_y = [*range(-230, 230, 40)]
    y = random.choice(car_y)
    return y


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.player_speed = 4
        self.shape("square")
        self.color(random_color())
        self.penup()
        self.shapesize(1, 2, 0)
        self.goto(random.randint(320, 1500), random_y())

    def speed_up(self):
        self.player_speed += 2

    def car_move(self):
        self.back(self.player_speed)
        if self.xcor() < -340:
            self.goto(random.randint(320, 1500), random_y())

