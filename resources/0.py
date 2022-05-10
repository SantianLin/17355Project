import turtle as t

t.pensize(4)
t.color("red")

t.seth(45)
for i in range(5):
    t.circle(-20,90)
    t.circle(20,90)
t.circle(-20,45)
t.fd(20)
t.circle(40,180)
t.fd(40)
t.done()
