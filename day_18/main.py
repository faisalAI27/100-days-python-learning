import random
from turtle import Turtle,Screen
timmy_the_turtle=Turtle()
colours=['red','green','blue','orange','black','brown','pink']
directions=[0,90,180,270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed(0)
for _ in range(200):
    timmy_the_turtle.color(random.choice(colours))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))
