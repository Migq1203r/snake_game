from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.write("Score: 0",font=("Arial",16,"bold"),align="center")
        self.hideturtle()
        
    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",font=("Arial",16,"bold"),align="center")