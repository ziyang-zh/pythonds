from random import randrange
from pythonds.basic import Stack
def flip():
	return randrange(2)

class HeaderNode:
	def __init__(self):
		self.next=None
		self.down=None

	def getNext(self):
		return self.next

	def getDown(self):
		return self.down

	def setNext(self,newnext):
		self.next=newnext

	def setDown(self,newdown):
		self.down=newdown

class DataNode:
	def __init__(self,key,value):
		self.key=key
		self.data=value
		self.next=None
		self.down=None

	def getKey(self):
		return self.key

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getDown(self):
		return self.down

	def setData(self,newdata):
		self.data=newdata

	def setNext(self,newnext):
		self.next=newnext

	def setDown(self,newdown):
		self.down=newdown

class SkipList:
	def __init__(self):
		self.head=None

	def __getitem__(self,key):
		return self.search(key)

	def __setitem__(self,key,value):
		if self.search(key):
			current=self.head
			found=False
			stop=False

			while not stop:
				if current==None:
					stop=True
				else:
					if current.getNext()==None:
						current=current.getDown()
					else:
						if current.getNext().getKey()==key:
							current.getNext().setData(value)
							current=current.getDown()    
						else:
							if key<current.getNext().getKey():
								current=current.getDown()
							else:
								current=current.getNext()
		else:
			print("error: key not exist!")

	def search(self,key):
		current=self.head
		found=False
		stop=False

		while not found and not stop:
			if current==None:
				stop=True
			else:
				if current.getNext()==None:
					current=current.getDown()
				else:
					if current.getNext().getKey()==key:
						found=True
					else:
						if key<current.getNext().getKey():
							current=current.getDown()
						else:
							current=current.getNext()

		if found:
			return current.getNext().getData()
		else:
			return None

	def insert(self,key,data):
		if self.head==None:
			self.head=HeaderNode()
			temp=DataNode(key,data)
			self.head.setNext(temp)
			top=temp

			while flip()==1:
				newhead=HeaderNode()
				temp=DataNode(key,data)
				temp.setDown(top)
				newhead.setNext(temp)
				newhead.setDown(self.head)
				self.head=newhead
				top=temp
		else:
			towerStack=Stack()
			current=self.head
			stop=False
			while not stop:
				if current==None:
					stop=True
				else:
					if current.getNext()==None:
						towerStack.push(current)
						current=current.getDown()
					else:
						if current.getNext().getKey()>key:
							towerStack.push(current)
							current=current.getDown()
						else:
							current=current.getNext()

			lowestLevel=towerStack.pop()
			temp=DataNode(key,data)
			temp.setNext(lowestLevel.getNext())
			lowestLevel.setNext(temp)
			top=temp

			while flip()==1:
				if towerStack.isEmpty():
					newhead=HeaderNode()
					temp=DataNode(key,data)
					temp.setDown(top)
					newhead.setNext(temp)
					newhead.setDown(self.head)
					top=temp
				else:
					nextLevel=towerStack.pop()
					temp=DataNode(key,data)
					temp.setDown(top)
					temp.setNext(nextLevel.getNext())
					nextLevel.setNext(temp)
					top=temp

	def delete(self,key):
		if self.search(key):
			current=self.head
			found=False
			stop=False

			while not stop:
				if current==None:
					stop=True
				else:
					if current.getNext()==None:
						current=current.getDown()
					else:
						if current.getNext().getKey()==key:
							val=current.getNext().getData()
							current.setNext(current.getNext().getNext())
							current=current.getDown()    
						else:
							if key<current.getNext().getKey():
								current=current.getDown()
							else:
								current=current.getNext()
			return val
		else:
			print("error: key not exist!")

	def keys(self):
		current_head=self.head
		while current_head.getDown():
			current_head=current_head.getDown()
						
		current=current_head.getNext()
		keysList=[]
		while current:
			keysList.append(current.getKey())
			current=current.getNext()
		return keysList

	def values(self):
		current_head=self.head
		while current_head.getDown():
			current_head=current_head.getDown()
						
		current=current_head.getNext()
		keysList=[]
		while current:
			keysList.append(current.getData())
			current=current.getNext()
		return keysList

	def traversal(self):
		current_head=self.head
		while current_head:
			current=current_head.getNext()
			while current:
				print(current.getKey(),current.getData(),end='\t')
				current=current.getNext()
			print(end='\n')
			current_head=current_head.getDown()

class Map:
	def __init__(self):
		self.collection=SkipList()

	def __contains__(self,key):
		return key in self.keys()

	def __getitem__(self,key):
		return self.collection[key]

	def __setitem__(self,key,value):
		self.collection[key]=value

	def put(self,key,value):
		self.collection.insert(key,value)

	def get(self,key):
		return self.collection.search(key)

	def pop(self,key):
		return self.collection.delete(key)

	def keys(self):
		return self.collection.keys()

	def values(self):
		return self.collection.values()

	def traversal(self):
		self.collection.traversal()

m=Map()
m.put(31,1)
m.put(77,7)
m.put(17,7)
m.put(54,4)
m.put(26,6)
m.put(65,5)
print(m.keys())
print(m.values())
print(m.get(31))
m.pop(31)
print(m.keys())
print(m.values())
print(31 in m)
print(77 in m)
print(m[26])
m[26]=36
print(m[26])
print(m.values())