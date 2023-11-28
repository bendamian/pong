from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(3, 1)
        self.color("white")
        self.color("white")
        self.penup()
        self.goto(350, 0)
