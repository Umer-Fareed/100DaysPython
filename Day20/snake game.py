import time
from turtle import Turtle, Screen
from snakes import Snake

screen = Screen()
screen.setup(600, 600)
screen.title("My Snake game ")
screen.tracer(0)
screen.bgcolor("black")


#create snake
snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()