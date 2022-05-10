import turtle as t
for i in range(100):
 t.fd(2*i)
 t.lt(90)
t.ht()
import turtle as t
n=int(input())
t.color("black","yellow")
t.ht()
t.begin_fill()
for i in range(n):
  t.fd(80) 
  t.lt(360/n)
t.end_fill()
t.done
