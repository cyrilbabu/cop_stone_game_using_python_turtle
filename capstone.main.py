from turtle import Screen
from player import Object
from car import Car
from scoreboard import Scoreboard

game = True

s = Screen()
s.setup(600, 600)
s.bgcolor("black")
s.tracer(0)

player = Object()
score = Scoreboard()

s.listen()
s.onkey(fun=player.move_up, key="Up")
s.onkey(fun=player.move_down, key="Down")

cars = []
for i in range(40):
    car = Car()
    cars.append(car)

while game:
    for move in cars:
        move.car_move()
        s.update()
        if player.ycor() > 240:
            score.update_scoreboard()
            player.reset_game()
            for speed in cars:
                speed.speed_up()
        if move.distance(player) <= 30 and move.ycor() + 10 >= player.ycor() >= move.ycor() - 10:
            score.game_over()
            print(move.ycor() + 10, move.ycor() - 10, player.ycor())
            game = False

s.exitonclick()
