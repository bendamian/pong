from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(2)
        self.color("white")
        self.penup()

    def move(self):
        x_core = self.xcor() + 5
        y_core = self.ycor() + 5
        self.goto(x_core, y_core)


