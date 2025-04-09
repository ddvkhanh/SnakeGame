from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_score()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.show_score()

    def increase(self):
        self.clear()
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, ALIGNMENT, FONT)

    def read_score(self):
        with open("data.txt") as f:
            return int(f.read())

    def write_score(self, score):
        with open("data.txt", mode="w") as f:
            f.write(f"{self.highscore}")

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_score(self.highscore)
        self.score = 0
        self.show_score()

