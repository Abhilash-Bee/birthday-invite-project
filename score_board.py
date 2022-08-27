import time
from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setposition(0, 260)
        self.color("white")
        self.score = 0
        with open("highest.txt") as high:
            self.highest_score = int(high.read())
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score:: {self.score} Highest Score:: {self.highest_score}",
                   align="center", font=("Arial", 20, "normal"))

    def update(self):
        if self.score > self.highest_score:
            with open("highest.txt", "w") as high:
                high.write(f"{self.score}")

        self.score = 0
        time.sleep(1)
        self.clear()
        self.__init__()

