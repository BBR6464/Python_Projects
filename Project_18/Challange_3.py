from turtle import Turtle, Screen
import random
timmy = Turtle()

colors = ["blue", "deep sky blue", "teal", "dark red", "magenta", "peach puff", "medium purple"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.left(angle)

for shape_sides_n in range(3,11):
    timmy.color(random.choice(colors))
    draw_shape(shape_sides_n)




screen = Screen()
screen.exitonclick()