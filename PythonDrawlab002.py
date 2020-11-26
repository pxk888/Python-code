#PythonDraw.py
import turtle
turtle.setup(1024,768,200,200)
turtle.pensize(5)
for i in range(0,4):
    turtle.fd(150)
    turtle.right(90)
    turtle.circle(-150,45)
    turtle.right(90)
    turtle.fd(150)
    turtle.right(45)
turtle.done()
