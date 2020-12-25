from pythonds.graphs import Graph,Vertex
from pythonds.basic import Queue

def buildGraph(wordfile):
	d={}
	g=Graph()
	wfile=open(wordfile,'r')
	for line in wfile:
		word=line[:-1]
		for i in range(len(word)):
			bucket=word[:i]+'_'+word[i+1:]
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket]=[word]

	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1!=word2:
					g.addEdge(word1,word2)
	return g

def bfs(g,start):
	start.setColor('gray')
	start.setDistance(0)
	start.setPred(None)
	vertQueue=Queue()
	vertQueue.enqueue(start)
	while (vertQueue.size()>0):
		currentVert=vertQueue.dequeue()
		for nbr in currentVert.getConnections():
			if (nbr.getColor()=='white'):
				nbr.setColor('grey')
				nbr.setDistance(currentVert.getDistance()+1)
				nbr.setPred(currentVert)
				vertQueue.enqueue(nbr)
		currentVert.setColor('Black')

def traverse(y):
	x=y
	while (x.getPred()):
		print(x.getId())
		x=x.getPred()
	print(x.getId())

g=buildGraph('fourletterwords.txt')
bfs(g,g.getVertex('FOOL'))
traverse(g.getVertex('SAGE'))