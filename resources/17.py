from turtle import *
setup(1500,300)
seth(-40)
penup()
goto(-250,-20)
pd()
width(20)
color("purple")
speed(10)
for i in range(8):
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
fd(40)
circle(20,180)
fd(40*2/3)

