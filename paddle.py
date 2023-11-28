from turtle import Turtle

x_position = 350
y_position = 0


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        pass

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        pass
