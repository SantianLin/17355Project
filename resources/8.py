import turtle
turtle.penup()
turtle.fd(-300)
turtle.pendown()
turtle.pensize(30)
turtle.pencolor("red")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(20,180)
turtle.fd(30)
turtle.done()