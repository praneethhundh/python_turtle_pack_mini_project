from turtle import Turtle,Screen
import random
t=Turtle()
s=Screen()
s.setup(height=500,width=500)
user_bet=s.textinput(title="make your pet",prompt="which turtle will win the race?what the color:")
colorsi=["red","blue","yellow","green","pink","orange"]
posi=[-90,-60,-30,0,30,60]
allturtle=[]
for i in range(0,6):
    t=Turtle(shape="turtle")
    t.color(colorsi[i])
    t.penup()
    t.goto(x=-180,y=posi[i])
    allturtle.append(t)
if user_bet:
    is_on_race=True
while(is_on_race):
    for tt in allturtle:
        if tt.xcor()>230:
            is_on_race=False
            winning=tt.pencolor()
            if winning==user_bet:
                print(f"you won {winning} bet same as you")
            else:
                print(f"you lost {winning} differnt bet as you")
        b=random.randint(1,10)
        tt.forward(b)
s.exitonclick()