from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, 'q')
screen.onkey(l_paddle.go_down, 'z')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #  Detect collision with wall
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        # need to bounce
        ball.bounce()

screen.exitonclick()
