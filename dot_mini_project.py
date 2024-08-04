import turtle as tk
import random
t=tk.Turtle()
tk.colormode(255)
import colorgram 
colors=colorgram.extract('image.png',30)
t.speed("fastest")
t.penup()
t.hideturtle()
colorslist=[  (203, 165, 108), (152, 74, 48), (234, 238, 243), 
             (52, 93, 124), (170, 153, 41), (223, 202, 136),
               (137, 32, 21), (132, 163, 185), (47, 121, 88),
                 (198, 91, 72), (15, 99, 73), (70, 47, 39),
                   (147, 179, 148), (98, 73, 75), (162, 142, 157), 
                   (234, 175, 164), (55, 46, 49), (184, 205, 172), 
                   (24, 81, 87), (38, 61, 74), (142, 22, 25),
                     (85, 146, 126), (45, 65, 85), (175, 91, 94), 
                     (214, 177, 183), (18, 70, 64), (109, 125, 151)]
t.setheading(225)
t.forward(300)
t.setheading(0)
no=100
for doti in range(1,no+1):
    t.dot(20,random.choice(colorslist))
    t.forward(50)
    
    if doti%10==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)