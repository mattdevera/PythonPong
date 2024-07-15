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
border.setposition(-300, -300)
border.pendown()
for _ in range(4):
    border.forward(600)
    border.left(90)
#scoreboard and timer
score = 0
seconds = 0
scoreboard = Turtle(visible = False)
scoreboard.color("white")
scoreboard.penup()
scoreboard.setposition(-290, 310)
scoreboard.write("Score {}".format(score), False, align = "left", font = ("Arial", 16, "normal"))
timer = Turtle(visible = False)
timer.color("white")
timer.penup()
timer.setposition(260, 310)
timer.write("Time {}".format(seconds), False, align = "left", font = ("Arial", 16, "normal"))
#player and computer paddles
#player paddle
player = Turtle("square", visible = False)
player.shapesize(0.5, 3)
player.speed("fastest")
player.setheading(90)
player.color("red")
player.penup()
player.setposition(-280, -250)
player.showturtle()
playerSpeed = 15
#computer paddle
computer = Turtle("square", visible = False)
computer.shapesize(0.5, 3)
computer.speed("fastest")
computer.setheading(90)
computer.color("blue")
computer.penup()
computer.setposition(280, 250)
computer.showturtle()
computerSpeed = 15
#ball
ball = Turtle("circle", visible = False)
ball.speed("fast")
ball.color("white")
ball.penup()
#ball.sety(265)
ball.showturtle()
ballSpeed = 15
ballChangeInX = 5
ballChangeInY = -5