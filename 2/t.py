import turtle 

t = turtle.Turtle()
t.pensize(3)
t.speed(0)

t.pencolor("blue")
for i in range(120):
    t.forward(350)
    t.left(111) # Let's go counterclockwise this time 
    
t.pencolor("red")
for i in range(120):
    t.forward(270)
    t.left(111)
    
t.pencolor("green")
for i in range(120):
    t.forward(230)
    t.left(111)

t.pencolor("black")
for i in range(119):
    t.forward(200)
    t.left(137)
#
t.reset()
for x in range(1, 38):
    t.forward(100)
    t.left(175)
#
t.reset()
t.color(1,0,0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()
t.color(0,0,0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()
t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.down()
t.circle(10)
t.end_fill()

#

turtle.done()
