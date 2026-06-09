from turtle import Turtle,Screen
import random

is_race_on=False

screen=Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make your bet",prompt="which turtle will win the race? Enter a color: ")


colors=['red','green','yellow','orange','blue','purple']
turtle_list=[]


for i in range(0,6):
    tim_i=Turtle(shape='turtle')
    tim_i.color(colors[i])
    tim_i.penup()
    tim_i.goto(x=-230, y=-100+(i*35))
    turtle_list.append(tim_i)

if user_bet:
    is_race_on=True
while is_race_on:
   
    for turtle in turtle_list:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f'you won! color is: {winning_color}')
            else:
                print(f'you have lost the color is: {winning_color}')
screen.exitonclick()