from turtle import Turtle, Screen
from turtle import *     # (*) For importing everything from turtle

t = Turtle()
t.shape("turtle")
t.color("red")

for _ in range(4):
    t.forward(100)
    t.right(90)

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# import heroes
# print(heroes.gen())











screen = Screen()
screen.exitonclick()