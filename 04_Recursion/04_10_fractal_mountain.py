from turtle import *
from random import randrange

def drawTriangle(myTurtle,points,degree,color):
	myTurtle.color(color)
	myTurtle.up()
	myTurtle.goto(points[0])
	if degree==0:
		myTurtle.down()
	myTurtle.goto(points[1])
	myTurtle.goto(points[2])
	myTurtle.goto(points[0])

def getMid(p1,p2):
	return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def fractalTriangle(myTurtle,points,degree):
	colormap=['blue','red','green','white','yellow','violet','orange']
	drawTriangle(myTurtle,points,degree,colormap[degree])
	if degree>0:
		fractalTriangle(myTurtle,[points[0],getMid(points[0],points[1]),getMid(points[0],points[2])],degree-1)
		fractalTriangle(myTurtle,[points[1],getMid(points[0],points[1]),getMid(points[1],points[2])],degree-1)
		fractalTriangle(myTurtle,[points[2],getMid(points[2],points[1]),getMid(points[0],points[2])],degree-1)
		fractalTriangle(myTurtle,[getMid(points[0],points[1]),getMid(points[0],points[2]),getMid(points[1],points[2])],degree-1)

def fractalMountain(myTurtle,degree):
	myPoints=[(0,0),(200,100),(100,200)]
	fractalTriangle(myTurtle,myPoints,degree)
	myPoints=[(100,200),(200,100),(300,200)]
	fractalTriangle(myTurtle,myPoints,degree)
	myPoints=[(400,50),(200,100),(300,200)]
	fractalTriangle(myTurtle,myPoints,degree)
	myPoints=[(100,200),(300,200),(250,400)]
	fractalTriangle(myTurtle,myPoints,degree)

myTurtle=Turtle()
myWin=myTurtle.getscreen()
fractalMountain(myTurtle,4)
myWin.exitonclick()