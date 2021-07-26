from turtle import Turtle, Screen


def draw_side():
    turtle.right(90)
    turtle.forward(100)


def draw_square():
    for side in range(0, 4):
        draw_side()


turtle = Turtle()
turtle.shape("classic")

draw_square()

screen = Screen()
screen.exitonclick()
