
from turtle import Turtle, Screen
import random


race_is_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which one will be win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-180, -100, -30, 30, 100, 150]
all_turtles = []


for _ in range(0, 6):
    tim = Turtle("turtle")
    tim.color(colors[_])
    tim.penup()
    tim.goto(x=-230, y=y_positions[_])
    all_turtles.append(tim)

if user_bet:
    race_is_on = True

while race_is_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you win {winning_color} turtle won the game")
            else:
                print(f"you lose the bet. {winning_color} turtle won the game")
        random_number = random.randint(0, 10)
        turtle.forward(random_number)

screen.exitonclick()