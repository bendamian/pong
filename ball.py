from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(2)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_core = self.xcor() + self.x_move
        y_core = self.ycor() + self.y_move
        self.goto(x_core, y_core)

    def bounce(self):
        self.y_move *= -1
