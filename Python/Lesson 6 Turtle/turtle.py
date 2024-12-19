import turtle 
turtle.Screen().bgcolor("Red")
sc = turtle.Screen()
sc.setup(300, 200)
turtle.title("This is my turtle window")
board = turtle.Turtle()
for i in range (4):
    board.foward(200)
    board.left(90)
    i =i+1