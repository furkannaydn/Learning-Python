import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("turtle python")


turtle_instanse=turtle.Turtle()
turtle_instanse.color("blue")

def shrinkingSquare(size):

 for i in range(4):
  turtle_instanse.forward(size)
  turtle_instanse.left(90)
  size=size-5

shrinkingSquare(150)
shrinkingSquare(90)
shrinkingSquare(70)

turtle.done()