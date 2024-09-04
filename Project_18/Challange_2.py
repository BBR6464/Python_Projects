from turtle import Turtle, Screen
tt_turtle_obj = Turtle()

for _ in range(4):
    for _ in range(15):
        tt_turtle_obj.forward(10)
        tt_turtle_obj.penup()
        tt_turtle_obj.forward(10)
        tt_turtle_obj.pendown()

    tt_turtle_obj.left(90)

screen = Screen()
screen.exitonclick()