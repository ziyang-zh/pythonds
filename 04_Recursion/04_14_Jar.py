class Jar:
	def __init__(self,label,v):
		self.label=label
		self.v=v
		self.current=0

	def __str__(self):
		return "jar "+self.label+": ("+str(self.current)+" / "+str(self.v)+")"

	def addFull(self):
		addv=self.v-self.current
		self.current=self.v
		return addv

	def pullAll(self):
		pullv=self.current
		self.current=0
		return pullv


jar1=Jar('A',4)
jar2=Jar('B',3)
print(jar1.label)
jar1.addFull()
print(jar1)
jar1.pullAll()
print(jar1)

