from turtle import Turtle


POS=[(-20,0),(-40,0),(-60,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self) -> None:
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        #creating snake
        for ded in POS:
            self.add_seg(ded)
        
        
    def add_seg(self,POS):
        
        t= Turtle()
        t.shape("square")
        t.color("white")
        t.pu()
        t.goto(POS)
        self.segments.append(t)
    
    def extend(self):
        self.add_seg(self.segments[-1].position())




    def move(self):
        
        #animation moving snake
        for seg in range(len(self.segments)-1,0,-1):
            newx=self.segments[seg-1].xcor()
            newy=self.segments[seg-1].ycor()
            self.segments[seg].goto(newx,newy)
        self.head.forward(20)
        
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

        


