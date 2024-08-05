from turtle import Turtle,Screen
t=Turtle()
s=Screen()
def forwardness():
    t.forward(100)
def backwardness():
    t.backward(100)
def turnleft():
    newhead=t.heading()-10
    t.setheading(newhead)
def turnright():
    newhead=t.heading()+10
    t.setheading(newhead)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
s.listen()
s.onkey(key="space",fun=forwardness)
s.onkey(backwardness,"w")
s.onkey(turnleft,'l')
s.onkey(turnright,'r')
s.onkey(clear,'c')
s.exitonclick()