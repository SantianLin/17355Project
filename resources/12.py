from turtle import *

setup(800,300)

seth(-40)

penup()

goto(-250,-20)
pd()

width(25)

color("blue")

for i in range(5):

  circle(40,80)

  circle(-40,80)

circle(40,80/2)

fd(40)

circle(20,180)

fd(40*2/3)
