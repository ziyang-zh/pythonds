from pythonds.basic import Stack
from turtle import *
import time

def drawDisk(t,length,width,x,y,color):
	tracer(0)
	t.fillcolor(color)
	t.up()
	t.goto(x-length/2,y-width/2)
	t.down()
	t.begin_fill()
	t.forward(length)
	t.left(90)
	t.forward(width)
	t.left(90)
	t.forward(length)
	t.left(90)
	t.forward(width)
	t.left(90)
	t.end_fill()
	update()
	tracer(1)

def drawHanoi(t,Towers):
	time.sleep(1)
	t.clear()

	width=20
	colormap=['white','red','orange','yellow','green','blue','violet']
	tempStack=Stack()
	
	for i in range(len(Towers)):
		for j in range(Towers[i].size()):
			tempStack.push(Towers[i].pop())

		for k in range(tempStack.size()):
			rank=tempStack.pop()
			Towers[i].push(rank)
			drawDisk(t,width*rank,width,200*(i-1),width*k,colormap[rank])

def moveDisk(t,Towers,fp,tp):
	disk=Towers[Towers_name.index(fp)].pop()
	Towers[Towers_name.index(tp)].push(disk)
	drawHanoi(t,Towers)

def moveTower(t,Towers,height,fromPole,toPole,withPole):
	if height>=1:
		moveTower(t,Towers,height-1,fromPole,withPole,toPole)
		moveDisk(t,Towers,fromPole,toPole)
		moveTower(t,Towers,height-1,withPole,toPole,fromPole)

height=6
Towers_name=['a','b','c']
Towers=[Stack() for i in range(3)]
for i in range(height):
	Towers[0].push(height-i)

t=Turtle()
t.hideturtle()
myWin=t.getscreen()
drawHanoi(t,Towers)
moveTower(t,Towers,height,Towers_name[0],Towers_name[2],Towers_name[1])
myWin.exitonclick()