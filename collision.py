from turtle import Turtle


class Collision(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()

    def game_over(self):
        self.write(f"Game Over! You Lose the Game!", font=("Arial", 16, "bold"), align="center")
