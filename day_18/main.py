import random
from turtle import Turtle,Screen
timmy_the_turtle=Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')
#MAKING DIFFERENT SHAPES.....


colours=['red','green','blue','orange','black','brown','pink']
def draw_shape(num_side):
    angle=360/num_side

    for _ in range(num_side):
        angle=360/num_side
        timmy_the_turtle.forward(130)
        timmy_the_turtle.right(angle)
    

for shape_side_n in range(3,11):
    timmy_the_turtle.color(random.choice(colours))
    draw_shape(shape_side_n)
