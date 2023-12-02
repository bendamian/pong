from turtle import Turtle


class ScoreBord(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,200)
        self.write(self.l_score, align='centre', font=("Calibre", 20,  "bold"))
