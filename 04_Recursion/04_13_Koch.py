from turtle import *

def drawKoch(myTurtle,length,degree):
	if degree==1:
		myTurtle.forward(length/3)
		myTurtle.left(60)
		myTurtle.forward(length/3)
		myTurtle.right(120)
		myTurtle.forward(length/3)
		myTurtle.left(60)
		myTurtle.forward(length/3)
	else:
		drawKoch(myTurtle,length/3,degree-1)
		myTurtle.left(60)
		drawKoch(myTurtle,length/3,degree-1)
		myTurtle.right(120)
		drawKoch(myTurtle,length/3,degree-1)
		myTurtle.left(60)
		drawKoch(myTurtle,length/3,degree-1)

def drawKochSnowflake(myTurtle,length,degree):
	drawKoch(myTurtle,length,degree)
	myTurtle.right(120)
	drawKoch(myTurtle,length,degree)
	myTurtle.right(120)
	drawKoch(myTurtle,length,degree)

myTurtle=Turtle()
myTurtle.width(3)
myTurtle.up()
myTurtle.goto(-400,200)
myTurtle.down()
myWin=myTurtle.getscreen()
drawKochSnowflake(myTurtle,3**6,5)
myWin.exitonclick()