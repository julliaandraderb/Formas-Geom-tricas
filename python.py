import turtle

t = turtle.Turtle()
t.color('blue')
t.width(10)

for i in range(4):
    t.forward(100)
    t.right(90)


t.penup()
t.forward(300)
t.pendown()

t.color('pink')
t.width(10)
t.forward(120)
t.left(120)
t.forward(120)
t.left(120)
t.forward(120)

t.penup()
t.forward(200)
t.pendown()

t.color('green')
t.circle(70)

t.penup()
t.forward(120)
t.pendown()
t.penup()
t.right(120)
t.forward(560)
t.pendown()

t.color('yellow')
t.width(10)
for i in range(6):
    t.forward(100)
    t.left(60)
turtle.done()

