from turtle import Turtle
ALIGN="center"
FONT=("Arial", 24, "normal")
class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0,260)
        self.increase()

    def increase(self):
        self.write(f"Score :{self.score}",align=ALIGN,font=FONT)
    def scoreupdate(self):
        self.score+=1
        self.clear()
        self.write(f"Score :{self.score}",align=ALIGN,font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGN,font=FONT)
        

    
        
        