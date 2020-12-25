from Node import Node

class OrderedList:
	def __init__(self):
		self.head=None

	def isEmpty(self):
		return self.head==None

	def add(self,item):
		current=self.head
		previous=None
		flag=True
		while current!=None and flag:
			if current.getData()>item:
				flag=False
			else:
				previous=current
				current=current.getNext() 

		temp=Node(item)
		if previous:
			temp.setNext(current)
			previous.setNext(temp)
		else:
			temp.setNext(self.head)
			self.head=temp

	def pop(self,pos=0):
		previous=None
		current=self.head
		flag=True
		for i in range(pos):
			if current.getNext()!=None:
				previous=current
				current=current.getNext()
			else:
				print("Error: Out of index!")
				flag=False
				break
				
		if flag:
			value=current.getData()
			if previous:
				previous.setNext(current.getNext())
			else:
				self.head=current.getNext()
			return value

	def remove(self,item):
		current=self.head
		previous=None
		found=False
		while not found and current.getNext()!=None:
			if current.getData()==item:
				found=True
			else:
				previous=current
				current=current.getNext()

		if previous==None:
			self.head=current.getNext()
		else:
			previous.setNext(current.getNext())

	def search(self,item):
		current=self.head
		found=False
		while current!=None and not found:
			if current.getData()==item:
				found=True
			else:
				current=current.getNext()
		return found

	def index(self,item):
		current=self.head
		pos=0
		while current!=None:
			if current.getData()==item:
				return pos
			else:
				current=current.getNext()
				pos=pos+1

	def length(self):
		current=self.head
		count=0
		while current!=None:
			count=count+1
			current=current.getNext()
		return count

	def traversal(self):
		current=self.head
		myList=[]
		while current!=None:
			myList.append(current.getData())
			current=current.getNext()
		return myList

mylist=OrderedList()
mylist.add(2)
mylist.add(1)
print(mylist.traversal())
mylist.add(3)
print(mylist.traversal())
mylist.add(0)
print(mylist.traversal())
mylist.add(0)
print(mylist.traversal())

print(mylist.pop())
print(mylist.traversal())
print(mylist.pop(3))
print(mylist.traversal())
print(mylist.pop(4))
mylist.remove(1)
print(mylist.traversal())
print(mylist.index(0))
print(mylist.search(2))
print(mylist.search(5))