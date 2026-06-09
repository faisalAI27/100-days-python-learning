from turtle import Turtle,Screen
screen=Screen()



screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
for i in range(0,3):
    tim=Turtle()
    tim.color('white')
    tim.shape('square')
    tim.goto(x=0+(i*20),y=0)




screen.exitonclick()