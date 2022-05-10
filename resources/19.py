import turtle

turtle.pen(speed=0)
turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()
turtle.seth(0)
length=400
while(length!=0):
    turtle.fd(length)
    turtle.left(90)
    length-=1.25
turtle.hideturtle()
turtle.done()
