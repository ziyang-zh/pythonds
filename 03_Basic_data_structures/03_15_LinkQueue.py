from Node import Node
class LinkQueue:
	def __init__(self):
		self.head=None
		self.rear=None
		self.count=0

	def __str__(self):
		current=self.head
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

	def enqueue(self,item):
		temp=Node(item)
		if self.count==0:
			self.head=temp
			self.rear=temp
		else:
			self.rear.setNext(temp)
			self.rear=self.rear.getNext()
		self.count+=1

	def dequeue(self):
		if self.count==0:
			return None
		else:
			item=self.head.getData()
			self.head=self.head.getNext()
			self.count-=1
			return item

	def size(self):
		return self.count


lq=LinkQueue()
print(lq)
print(lq.isEmpty())
for i in range(3):
	lq.enqueue(i)
	print(lq,lq.size())
for i in range(4):
	print(lq.dequeue())
	print(lq)
