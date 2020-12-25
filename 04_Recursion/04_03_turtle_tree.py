from turtle import *
import random

def drawSpiral(myTurtle,lineLen):
	if lineLen>0:
		myTurtle.forward(lineLen)
		myTurtle.right(90)
		drawSpiral(myTurtle,lineLen-5)

def tree(t,branchLen):
	t.pensize(branchLen//8)
	t.color('brown')
	if branchLen<20:
		t.color('green')
		t.pensize(branchLen/3)
	
	if branchLen > 5:
		leftAngle=random.randrange(30,46)
		rightAngle=random.randrange(15,31)
		t.forward(branchLen)
		t.right(rightAngle)
		tree(t,branchLen-random.randrange(12,18))
		t.left(leftAngle)
		tree(t,branchLen-random.randrange(7,13))
		t.right(leftAngle-rightAngle)
		t.up()
		t.backward(branchLen)
		t.down()

#drawSpiral(myTurtle,100)

t=Turtle()
myWin=t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
tree(t,110)
myWin.exitonclick()
