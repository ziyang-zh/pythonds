class Node:
	def __init__(self,initdata):
		self.data=initdata
		self.next=None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data=newdata

	def setNext(self,newnext):
		self.next=newnext

class UnorderedList:
	def __init__(self):
		self.head=None
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
		return self.head==None

	def length(self):
		return self.count

	def add(self,item):
		temp=Node(item)
		temp.setNext(self.head)
		self.head=temp
		self.count+=1

	def append(self,item):
		current=self.head
		if self.count==0:
			self.add(item)
		else:
			for i in range(self.count-1):
				current=current.getNext()
			current.setNext(Node(item))			
			self.count+=1

	def insert(self,item,pos):
		previous=None
		current=self.head

		if pos>self.count:
			print("Error: Out of index!")
		else:
			for i in range(pos):
				previous=current
				current=current.getNext()

			temp=Node(item)
			temp.setNext(current)
			if previous:
				previous.setNext(temp)
			else:
				self.head=temp
			self.count+=1

	def pop(self,pos=0):
		previous=None
		current=self.head

		if pos>self.count:
			print("Error: Out of index!")
		else:
			for i in range(pos):
				previous=current
				current=current.getNext()

			value=current.getData()
			if previous:
				previous.setNext(current.getNext())
			else:
				self.head=current.getNext()
			self.count-=1
			return value

	def remove(self,item):
		current=self.head
		previous=None

		for i in range(self.count):
			if current.getData()==item:
				if previous==None:
					self.head=current.getNext()
				else:
					previous.setNext(current.getNext())
				self.count-=1
				return True
			else:
				previous=current
				current=current.getNext()
		
		print("Error: Not found ["+str(item)+"]!")
		return False

	def search(self,item):
		current=self.head
		for pos in range(self.count):
			if current.getData()==item:
				return True
			else:
				current=current.getNext()
		print("Error: Not found ["+str(item)+"]!")
		return False

	def index(self,item):
		current=self.head
		for pos in range(self.count):
			if current.getData()==item:
				return pos
			else:
				current=current.getNext()
		print("Error: Not found ["+str(item)+"]!")
		return False

	def slice(self,start,end):
		subqueue=UnorderedList()
		current=self.head

		if start>self.count or end>self.count:
			print("Error: Out of index!")
		elif start>=end:
			print("Error: Input error!")
		else:
			for i in range(start):
				current=current.getNext()
			for i in range(end-start):
				subqueue.append(current.getData())
				current=current.getNext()
		return subqueue

mylist=UnorderedList()

mylist.add(1)
mylist.append(2)
mylist.append(3)
print(mylist)

mylist.insert(0,0)
mylist.insert(0,2)
mylist.insert(10,100)
print(mylist)

print(mylist.pop())
print(mylist)
print(mylist.pop(3))
print(mylist)
print(mylist.pop(4))

mylist.remove(2)
mylist.remove(10)
print(mylist)

print(mylist.search(0))
print(mylist.search(5))

print(mylist.index(0))
print(mylist.index(1))
print(mylist.index(2))

print("slice")
mylist=UnorderedList()
mylist.append(0)
mylist.append(1)
mylist.append(2)
mylist.append(3)
slice_list=mylist.slice(0,1)
print(mylist)
print(slice_list)