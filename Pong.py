from turtle import Turtle, Screen

#implementation for the display
#screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
#border
border = Turtle(visible = False)
border.speed("fastest")
border.color("white")
border.pensize(3)
border.penup()
border.setposition(-300, 300)
border.pendown()
for _ in range(4):
    border.forward(600)
    border.left(90)