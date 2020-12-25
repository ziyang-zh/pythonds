from Node import Node
class LinkStack:
	def __init__(self):
		self.head=None
		self.count=0

	def __str__(self):
		if self.count==0:
			output='[]'
		else:
			output='['
			current=self.head
			for i in range(self.count):
				output+=str(current.getData())+', '
				current=current.getNext()
			output=output[:-2]+']'
		return output

	def isEmpty(self):
		return self.count==0

	def push(self,item):
		temp=Node(item)
		temp.setNext(self.head)
		self.head=temp
		self.count+=1

	def pop(self):
		if self.count>0:
			temp=self.head
			self.head=temp.getNext()
			self.count-=1
			return temp.getData()
		else:
			return None

	def peek(self):
		if self.count==0:
			return None
		else:
			temp=self.head
			return temp.getData()

	def size(self):
		return self.count

ls=LinkStack()
print(ls.isEmpty())
print(ls)
print(ls.pop())
print(ls)
print(ls.peek())
print(ls.size())