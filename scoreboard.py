from turtle import Turtle

FONT = ("Courier", 13, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(x=0, y=280)
        self.update_score()
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")

        self.score = 0
        self.update_score()

    def increment_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        print(self.score, self.high_score)
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align="center", font=FONT)
