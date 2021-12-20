from turtle import Turtle

from random import randint as r


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed(0)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.location()

    def location(self):
        self.setposition(r(-280, 270), r(-280, 270))
