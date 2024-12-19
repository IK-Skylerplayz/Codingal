import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.speed(5)

def draw_shape(sides, length, fill_color):
    pen.fillcolor(fill_color)
    pen.begin_fill()
    for _ in range(sides):
        pen.forward(length)
        pen.left(360 / sides)
    pen.end_fill()

pen.penup()
pen.goto(-200, 100)
pen.pendown()
draw_shape(3, 100, "yellow")

pen.penup()
pen.goto(50, 100)
pen.pendown()
pen.fillcolor("red")
pen.begin_fill()
for _ in range(2):
    pen.forward(150)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
pen.end_fill()

pen.penup()
pen.goto(-75, -100)
pen.pendown()
draw_shape(6, 70, "green")

pen.hideturtle()
screen.mainloop()
