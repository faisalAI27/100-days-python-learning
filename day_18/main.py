import random
import turtle as t

timmy_the_turtle=t.Turtle()
colours=['red','green','blue','orange','black','brown','pink']
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    new_color=(r,g,b)
    return new_color
#-------------------------------------
timmy_the_turtle.speed('fastest')


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+ size_of_gap)
draw_spirograph(10)

screen=t.Screen()
screen.exitonclick()