from turtle import Turtle


class Object(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.shapesize(1, 1, 0)
        self.penup()
        self.left(90)
        self.goto(0, -280)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.back(20)

    def reset_game(self):
        self.goto(0, -280)
