import turtle
turtle.setup(800,300)
turtle.seth(-40)
turtle.penup()
turtle.goto(-250,-20)
turtle.pendown()
turtle.width(25)
turtle.color("green")
for i in range(5):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(20,180)
turtle.fd(40*2/3)
turtle.done
