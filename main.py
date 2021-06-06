from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

user_bet = screen.textinput(title="Make your best", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtle_list = []

y = -150
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.setposition(x=-200, y=y)
    turtle_list.append(new_turtle)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            break

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if winning_color == user_bet:
    print(f"You've won! The {winning_color} turtle is the winner!")
else:
    print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()
