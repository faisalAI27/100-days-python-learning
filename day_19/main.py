from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()

def move_backword():
    tim.backward(10)

def move_forward():
    tim.forward(10)

def counter_clock():
    tim.left(10)


def clock_wise():
    tim.right(10)

def clear():
    tim.clear
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backword)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=clear)

screen.listen()
screen.exitonclick()