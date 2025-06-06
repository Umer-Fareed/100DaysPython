from turtle import Turtle , Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("make your bet", prompt= "which turtle "
                                          "win the race: ")
colors = ["red", "orange" ,"yellow" , "green", "blue", "purple"]
y_positions = [-70 , -40, -10 , 20, 50, 80]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} turtle is winner !")
            else:
                print(f"you've lost! the {winning_color} turtle is he winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()