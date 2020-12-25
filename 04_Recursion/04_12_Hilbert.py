from turtle import *

def drawLeft(myTurtle,n,length):
    if n>0:
        myTurtle.right(90)
        drawRight(myTurtle,n-1,length)
        myTurtle.forward(length)
        myTurtle.left(90)
        drawLeft(myTurtle,n-1,length)
        myTurtle.forward(length)
        drawLeft(myTurtle,n-1,length)
        myTurtle.left(90)
        myTurtle.forward(length)
        drawRight(myTurtle,n-1,length)
        myTurtle.right(90)

def drawRight(myTurtle,n,length):
    if n>0:
        myTurtle.left(90)
        drawLeft(myTurtle,n-1,length)
        myTurtle.forward(length)
        myTurtle.right(90)
        drawRight(myTurtle,n-1,length)
        myTurtle.forward(length)
        drawRight(myTurtle,n-1,length)
        myTurtle.right(90)
        myTurtle.forward(length)
        drawLeft(myTurtle,n-1,length)
        myTurtle.left(90)

myTurtle=Turtle()
myTurtle.width(3)
myWin=myTurtle.getscreen()
drawLeft(myTurtle,4,15)
myWin.exitonclick()