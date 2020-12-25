from pythonds.graphs import Graph,Vertex

def posToNodeId(row,column,board_size):
	return (row*board_size)+column

def legalCoord(x,bdSize):
	if x>=0 and x<bdSize:
		return True
	else:
		return False

def genLeagalMoves(x,y,bdSize):
	newMoves=[]
	movesOffsets=[(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]
	for i in movesOffsets:
		newX=x+i[0]
		newY=y+i[1]
		if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
			newMoves.append((newX,newY))
	return newMoves

def knightGraph(bdSize):
	ktGraph=Graph()
	for row in range(bdSize):
		for col in range(bdSize):
			nodeId=posToNodeId(row,col,bdSize)
			newPositions=genLeagalMoves(row,col,bdSize)
			for e in newPositions:
				nid=posToNodeId(e[0],e[1],bdSize)
				ktGraph.addEdge(nodeId,nid)
	return ktGraph

def orderByAvail(n):
	resList=[]
	for v in n.getConnections():
		if v.getColor()=='white':
			c=0
			for w in v.getConnections():
				if w.getColor()=='white':
					c=c+1
			resList.append((c,v))
	resList.sort(key=lambda x:x[0])
	return [y[1] for y in resList]

def knightTour(n,path,u,limit):
	u.setColor('gray')
	path.append(u)
	if n<limit:
		nbrList=orderByAvail(u)
		i=0
		done=False

		while i<len(nbrList) and not done:
			if nbrList[i].getColor()=='white':
				done=knightTour(n+1,path,nbrList[i],limit)
				i=i+1
			if not done:
				path.pop()
				u.setColor('white')
	else:
		done=True
	return done
n=5
g=knightGraph(n)
path=[]
knightTour(0,path,g.getVertex(0),4)
for i in g:
	print(i)
