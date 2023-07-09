from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score import Score


s=Screen()
#setting screen
s.setup(width=600,height=600)
s.bgcolor("black")
s.tracer(0)

snake=Snake()
food=Food()
scores=Score()
s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")
#moving snake
game_on=True
while game_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scores.scoreupdate()

    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        game_on=False
        scores.gameover()
    for segment in snake.segments[1:]:
       
        if snake.head.distance(segment) < 10:
            game_on=False
            scores.gameover()

s.exitonclick()