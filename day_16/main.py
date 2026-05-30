#just an example for better understanding.
#import another_module
#print(another_module.another_variable)

#first way to import the turtle module
#import turtle
#timmy=turtle.Turtle()
#print(timmy)

#another way to import the turtle module
#class is represented by capital letter.
#from turtle import Turtle,Screen

#timmy=Turtle()
#timmy.shape("turtle")
#timmy.color("coral")
#timmy.forward(100)

#print(timmy)
#my_screen=Screen()
#my_screen.exitonclick()
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table.align)
table.align="l"
print(table)
print(table.align)