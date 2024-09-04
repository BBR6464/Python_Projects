import turtle as t
import random

tom = t.Turtle()

colors = ["blue", "deep sky blue", "teal", "dark red", "magenta", "peach puff", "medium purple"]
direction = [0, 90, 180, 270]
tom.pensize(15)
tom.speed("fastest")

for _ in range(200):
    tom.color(random.choice(colors))
    tom.forward(30)
    tom.setheading(random.choice(direction))



screen = Screen()
screen.exitonclick()