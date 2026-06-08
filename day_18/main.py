import random
import turtle as t

timmy_the_turtle=t.Turtle()
colours=['red','green','blue','orange','black','brown','pink']

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    new_color=(r,g,b)
    return new_color

directions=[0,90,180,270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed(0)
t.colormode(255)

for _ in range(200):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))
