######################################################################
# Author: Abdirahman Mohamed
# Username: mohameda
#

# Assignment: A2: Loopy Turtles
# Purpose: To very simply demonstrate the turtle library to demo shapes

######################################################################
# Acknowledgements:

#

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle # allows us to use the turtles library
wn = turtle.Screen()
wn.bgcolor('Red')

turtle.colormode(255)       # change color modes

wn = turtle.Screen()        # make screen close cleanly
wn.bgcolor('#DDDDDD')       # Sets background to gray

'''Draws a house on the screen'''
shape = turtle.Turtle()
shape.hideturtle()

#make roof
shape.color('red')
shape.begin_fill()          # Tells Python to fill the shape with a color when done
for side in range(3):
    shape.forward(300)
    shape.left(120)
shape.end_fill()            # Tells Python the shape is complete; now fill it
shape.up()

'''Make main house rectangle'''
shape.color('#eef442')
shape.begin_fill()
for side in range(2):
    shape.forward(300)
    shape.right(90)
    shape.forward(400)
    shape.right(90)
# shape.fill(False)
shape.end_fill()

'''Draws a window on the screen'''                 #The windows on the house make me smile because I like to see sunrise and sunset.
shakl = turtle.Turtle()
shakl.color('#f44253')
for side in range (2):
    shakl.forward(100)
    shakl.right(90)
    shakl.forward(140)
    shakl.right(90)
shakl.up()
'''Draws a window on the screen'''                  #I added another window
nakl = turtle.Turtle()
nakl.color ('#f44289')

for side in range (1):
    nakl.forward(100)
    nakl.right(90)
    nakl.forward(140)
    nakl.left(90)
    nakl.forward(100)
    nakl.left(90)
    nakl.forward(140)
    nakl.left(90)
    nakl.forward(100)

nakl.down()
'''Draws a circle on the screen'''
nakl.color('#42eef4')
for side in range (1):
    nakl.forward(100)
    nakl.right(90)
    nakl.forward(10)
    nakl.left(90)
    nakl.forward(50)

nakl.up()

tess = turtle.Turtle()                   #The line on the tringle I thought of it like a ketchup on a turkey sandwich.
tess.color('blue')
tess.pensize(20)
tess.penup()
tess.goto(0,0)
#tess.left(0)
tess.forward(150)
tess.left(90)
tess.forward(240)
tess.pendown()
tess.left(180)

for i in range (5):
    tess.forward(2)
    tess.right(90)
    tess.forward(10)
    tess.left(90)
    tess.forward(20)



"""mysize = 0
for d in range(5):
    tess.forward(mysize)
    mysize += 20
"""
''' Write text to the screen '''
shape.color("#0F00F0")
shape.setpos(40,100)
shape.write("Mi casa",move=False,align='center',font=("Arial",30,("bold","normal"))) #Changed the My house from English to Spanish

wn.exitonclick()
