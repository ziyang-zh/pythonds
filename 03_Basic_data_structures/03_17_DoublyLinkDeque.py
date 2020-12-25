class DoublyNode:
	def __init__(self,initdata):
		self.data=initdata
		self.prior=None
		self.next=None

	def __str__(self):
		return str(self.data)

	def getData(self):
		return self.data

	def getPrior(self):
		return self.prior

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data=newdata

	def setPrior(self,newprior):
		self.prior=newprior

	def setNext(self,newnext):
		self.next=newnext

class DoublyLinkDeque:
	def __init__(self):
		self.front=None
		self.rear=None
		self.count=0

	def __str__(self):
		current=self.front
		if self.count==0:
			output='[]'
		else:
			output='['
			for i in range(self.count):
				output+=str(current.getData())+', '
				current=current.getNext()
			output=output[:-2]+']'
		return output

	def isEmpty(self):
		return self.count==0

	def addFront(self,item):
		temp=DoublyNode(item)
		if self.count==0:
			self.front=temp
			self.rear=temp
		else:
			temp.setNext(self.front)
			self.front.setPrior(temp)
			self.front=temp
		self.count+=1

	def addRear(self,item):
		temp=DoublyNode(item)
		if self.count==0:
			self.front=temp
			self.rear=temp
		else:
			temp.setPrior(self.rear)
			self.rear.setNext(temp)
			self.rear=temp
		self.count+=1

	def removeFront(self):
		if self.count==0:
			return None
		else:
			item=self.front.getData()
			self.front=self.front.getNext()
			if self.front:
				self.front.setPrior(None)
			self.count-=1
			return item

	def removeRear(self):
		if self.count==0:
			return None
		else:
			item=self.rear.getData()
			self.rear=self.rear.getPrior()
			if self.rear:
				self.rear.setNext(None)
			self.count-=1
			return item

	def size(self):
		return self.count

ld=DoublyLinkDeque()
print(ld)
print(ld.isEmpty())
for i in range(4):
	ld.addRear(i)
	print(ld,ld.size())
	ld.addFront(i)
	print(ld,ld.size())
for i in range(5):
	print(ld.removeFront())
	print(ld.removeRear())
	print(ld)
