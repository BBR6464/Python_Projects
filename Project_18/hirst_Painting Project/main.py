# import colorgram
#
# rgb_color = []
# colors = colorgram.extract('image.jpeg', 38)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)


import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(237, 252, 244), (240, 245, 251), (243, 234, 57), (197, 8, 37), (214, 158, 86), (240, 233, 2), (36, 212, 76), (47, 81, 167), (26, 37, 164), (233, 45, 137), (204, 68, 19), (19, 146, 22), (219, 135, 188), (195, 36, 107), (182, 14, 9), (228, 152, 8), (60, 13, 9), (67, 11, 26), (99, 175, 211), (104, 202, 128), (237, 162, 206), (108, 232, 186), (75, 83, 220), (17, 16, 41), (10, 95, 61), (207, 88, 58), (172, 175, 239), (10, 74, 48), (6, 230, 241), (234, 173, 161), (254, 4, 45), (0, 251, 226), (77, 232, 250), (18, 43, 246), (2, 77, 119)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()