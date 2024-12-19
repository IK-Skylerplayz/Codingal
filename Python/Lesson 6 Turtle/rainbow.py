import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(1)

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

def draw_rainbow_spiral():
    num_colors = 360
    colors = [colorsys.hsv_to_rgb(i / num_colors, 1, 1) for i in range(num_colors)]
    
    for i in range(360):
        pen.pencolor(colors[i % num_colors])
        pen.forward(i * 2 / 100)
        pen.right(59)

draw_rainbow_spiral()
pen.hideturtle()
screen.mainloop()
