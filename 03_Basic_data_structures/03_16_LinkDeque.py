from Node import Node
class LinkDeque:
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
		temp=Node(item)
		if self.count==0:
			self.front=temp
			self.rear=temp
		else:
			temp.setNext(self.front)
			self.front=temp
		self.count+=1

	def addRear(self,item):
		temp=Node(item)
		if self.count==0:
			self.front=temp
			self.rear=temp
		else:
			self.rear.setNext(temp)
			self.rear=temp
		self.count+=1

	def removeFront(self):
		if self.count==0:
			return None
		else:
			item=self.front.getData()
			self.front=self.front.getNext()
			self.count-=1
			return item

	def removeRear(self):
		if self.count==0:
			return None
		else:
			item=self.rear.getData()
			new_rear=self.front
			for i in range(self.count-2):
				new_rear=new_rear.getNext()
			self.rear=new_rear
			self.rear.setNext(None)
			self.count-=1
			return item

	def size(self):
		return self.count


ld=LinkDeque()
print(ld)
print(ld.isEmpty())
for i in range(3):
	ld.addRear(i)
	print(ld,ld.size())
	ld.addFront(i)
	print(ld,ld.size())
for i in range(4):
	print(ld.removeRear())
	print(ld.removeFront())
	print(ld)
