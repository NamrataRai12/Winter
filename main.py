import turtle
import random
screen= turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')

t = turtle.Turtle()
t.hideturtle()
t2 = turtle.Turtle()
t2.hideturtle()
t3 = turtle.Turtle()
t3.hideturtle()

t.pencolor('black')
t.penup()
t.goto(0,200)
t.pendown()
t.write("Happy Holidays!", font=("arial", 18, "bold"), align="center")


t = turtle.Turtle()
t.speed(0)
t.pensize(1)
for i in range(500):
   t.pencolor('snow')
   x= random.randint(-1000,1000)
   y = random.randint(-100,600)
   t.penup()
   t.goto(x,y)
   t.pendown()
   t.dot()


t_ground =turtle.Turtle()
t_ground.fillcolor('snow1')
t_ground.pencolor('snow1')
t_ground.speed(0)
t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()

#tree
t.pencolor('forestgreen')
t.fillcolor('forestgreen')
t.penup()
t.goto(50,50)#1/4
t.pendown()
t.begin_fill()
t.goto(150,50)
t.goto(100,150)
t.goto(50,50)
t.end_fill()

t.fillcolor('forestgreen')
t.penup()
t.goto(50,0)#1/4
t.pendown()
t.begin_fill()
t.goto(150,0)
t.goto(100,150)
t.goto(50,0)
t.end_fill()

t.fillcolor('forestgreen')
t.penup()
t.goto(50,-50)#1/4
t.pendown()
t.begin_fill()
t.goto(150,-50)
t.goto(100,150)
t.goto(50,-50)
t.end_fill()

shift_x=100
shift_y=-50
# #star
t.pencolor("goldenrod3")
t.fillcolor("gold1")
t.penup()
t.begin_fill()
t.goto(-30+shift_x,220+shift_y)
t.pendown()
t.goto(30+shift_x,220+shift_y)
t.goto(-20+shift_x,190+shift_y)
t.goto(0+shift_x,240+shift_y)
t.goto(20+shift_x,190+shift_y)
t.goto(-30+shift_x,220+shift_y)
t.end_fill()

t.pencolor('saddle brown')
t.fillcolor('saddle brown')


t.penup()
t.goto(90,-100)
t.pendown()
t.begin_fill()
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()
#presents
t.penup()
t.goto(150, -100)
t.fillcolor('purple')
t.pensize(2)
t.pendown()
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.end_fill()

t.penup()
t.goto(165, -50)
t.fillcolor('yellow')
t.pendown()
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(15)
t.left(90)
t.forward(50)
t.left(90)
t.forward(15)
t.end_fill()

t.pencolor('yellow')
t.pensize(2)
t.penup()
t.goto(165,-30)
t.pendown()
t.circle(10)
t.penup()
t.goto(175,-30)
t.pendown()
t.circle(10)
#House
t.pencolor('sienna')
t.penup()
t.goto(-100,40)
t.fillcolor('lightsalmon4')
t.pendown()
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(150)
t.left(90)
t.forward(200)
t.left(90)
t.forward(150)
t.end_fill()

t.pencolor('sienna')
t.fillcolor('saddle brown')
t.begin_fill()
t.penup()
t.goto(-175,-110)
t.pendown()
t.begin_fill()
t.forward(75)
t.left(90)
t.forward(50)
t.left(90)
t.forward(75)
t.left(90)
t.forward(50)
t.left(90)
t.penup()
t.end_fill()

t.fillcolor('burlywood')
t.goto(-300,40)#1/4
t.pendown()
t.begin_fill()
t.goto(-100,40)
t.goto(-200,150)
t.goto(-300,40)
t.penup()
t.end_fill()


t.penup()
t.goto(-170,0 )
t.pencolor('green')
t.fillcolor('green')
t.pendown()
t.begin_fill()
t.circle(28)
t.end_fill()

t.penup()
t.goto(-183,0)
t.pencolor('green')
t.fillcolor('lightsalmon4')
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()
t.penup()


#cloud
t.goto(0,300)
t.pencolor('white')
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(50)
t.goto(-55,285)
t.circle(40)
t.goto(45,285)
t.circle(40)
t.end_fill()
t.penup()

#snowman

t.fillcolor('white')
t.goto(400,-55)
t.pendown()
t.begin_fill()
t.circle(55)
t.penup()
t.end_fill()

t.fillcolor('white')
t.goto(390,0)
t.pendown()
t.begin_fill()
t.circle(45)
t.penup()
t.end_fill()

t.fillcolor('white')
t.goto(380,60)
t.pendown()
t.begin_fill()
t.circle(35)
t.penup()
t.end_fill()

#eyes and mouth
t.penup()
t.goto(335,60)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(4)
t.end_fill()


t.penup()
t.goto(360,60)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(4)
t.end_fill()


t.penup()
t.goto(335,45)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(2)
t.end_fill()


t.penup()
t.goto(340,40)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(2)
t.end_fill()


t.penup()
t.goto(345,38)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(2)
t.end_fill()


t.penup()
t.goto(350,40)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(2)
t.end_fill()


t.penup()
t.goto(355,45)
t.pencolor('black')
t.fillcolor('black')
t.pendown()
t.begin_fill()
t.circle(2)
t.end_fill()

t.penup()
t.goto(0,0)






#this is last line of code
turtle.done()
