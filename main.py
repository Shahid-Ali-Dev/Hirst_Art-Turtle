from turtle import Turtle, Screen, colormode
import random

colormode(255)

new_lst = [
    (197, 13, 34), (209, 14, 9), (232, 227, 5), (195, 69, 22), (34, 90, 185),
    (232, 150, 45), (44, 211, 74), (34, 31, 150), (17, 22, 55), (66, 10, 48),
    (242, 40, 143), (68, 201, 227), (15, 205, 221), (62, 22, 11), (218, 23, 108),
    (228, 162, 10), (18, 153, 24), (97, 75, 10), (243, 62, 20), (221, 140, 198),
    (74, 239, 163), (248, 11, 8), (11, 97, 62), (71, 217, 157), (6, 38, 33)
]

turtle = Turtle()
screen = Screen()
turtle.hideturtle()
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

for i in range(1, 101):
    turtle.dot(10, random.choice(new_lst))  
    turtle.forward(50)

    if i % 10 == 0:
        turtle.speed("fastest")
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen.exitonclick()
