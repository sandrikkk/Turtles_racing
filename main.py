import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
tamashi = False
choice = screen.textinput(title="Gaakete Fsoni !", prompt="Romeli ku moigebs rbolas ?")
colors = ["black", "purple", "orange", "green", "pink", "blue"]
y_coordinats = [-68,-40,-10,20,50,80]
all_turtles = []

for index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinats[index])
    all_turtles.append(new_turtle)

if choice:
    tamashi = True

while tamashi:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            mogebuli_feri = turtle.pencolor()
            tamashi = False
            if mogebuli_feri == choice:
                print("Tqven Moiget ! Gamarjvebuli Feria:",mogebuli_feri)
            else:
                print("Tqven Damarcxdit ! Gamarjvebuli Feria:",mogebuli_feri)

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
