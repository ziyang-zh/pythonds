from pythonds.basic import Stack

class TreeNode:
	def __init__(self,key,val,left=None,right=None,parent=None):
		self.key=key
		self.payload=val
		self.leftChild=left
		self.rightChild=right
		self.parent=parent
		self.balanceFactor=0
		self.ltag=None
		self.rtag=None

	def __iter__(self):
		if self:
			if self.hasLeftChild():
				for elem in self.leftChild:
					yield elem
			yield self.key
			if self.hasRightChild():
				for elem in self.rightChild:
					yield elem

	def hasLeftChild(self):
		return self.leftChild!=None

	def hasRightChild(self):
		return self.rightChild!=None

	def isLeftChild(self):
		return self.parent!=None and self.parent.leftChild==self

	def isRightChild(self):
		return self.parent!=None and self.parent.rightChild==self

	def isRoot(self):
		return self.parent==None

	def isLeaf(self):
		return not (self.leftChild or self.rightChild)

	def hasAnyChildren(self):
		return self.leftChild!=None or self.rightChild!=None

	def hasBothChildren(self):
		return self.leftChild and self.rightChild

	def replaceNodeData(self,key,value,lc,rc):
		self.key=key
		self.payload=value
		self.leftChild=lc
		self.rightChild=rc
		if self.hasLeftChild():
			self.leftChild.parent=self
		if self.hasRightChild():
			self.rightChild.parent=self

	def findMin(self):
		current=self
		while current.hasLeftChild():
			current=current.leftChild
		return current

	def findSuccessor(self):
		succ=None
		if self.hasRightChild():
			succ=self.rightChild.findMin()
		else:
			if self.parent!=None:
				if self.isLeftChild():
					succ=self.parent
				else:
					self.parent.rightChild=None
					succ=self.parent.findSuccessor()
					self.parent.rightChild=self
		return succ

	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftChild=None
			else:
				self.parent.rightChild=None
		elif self.hasLeftChildren():
			if self.isLeftChild():
				self.parent.leftChild=self.leftChild
			else:
				self.parent.rightChild=self.leftChild
			self.leftChild.parent=self.parent
		else:
			if self.isLeftChild():
				self.parent.leftChild=self.rightChild
			else:
				self.parent.rightChild=self.rightChild
			self.rightChild.parent=self.parent

class BinarySearchTree:
	def __init__(self):
		self.root=None
		self.size=0

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	def __setitem__(self,k,v):
		self.put(k,v)

	def __getitem__(self,key):
		return self.get(key)

	def __contains__(self,key):
		if self._get(key,self.root):
			return True
		else:
			return False

	def length(self):
		return self.size

	def _put(self,key,val,currentNode):
		if key<currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key,val,currentNode.leftChild)
			else:
				currentNode.leftChild=TreeNode(key,val,parent=currentNode)
		elif key>currentNode.key:
			if currentNode.hasRightChild():
				self._put(key,val,currentNode.rightChild)
			else:
				currentNode.rightChild=TreeNode(key,val,parent=currentNode)
		else:
			self._put(key+1,val,self.root)

	def put(self,key,val):
		if self.root:
			self._put(key,val,self.root)
		else:
			self.root=TreeNode(key,val)
		self.size=self.size+1

	def _get(self,key,currentNode):
		if not currentNode:
			return None
		elif currentNode.key==key:
			return currentNode
		elif key<currentNode.key:
			return self._get(key,currentNode.leftChild)
		else:
			return self._get(key,currentNode.rightChild)

	def get(self,key):
		if self.root:
			res=self._get(key,self.root)
			if res:
				return res.payload
			else:
				return None

	def remove(self,currentNode):
		if currentNode.isLeaf():
			if currentNode==currentNode.parent.leftChild:
				currentNode.parent.leftChild=None
			else:
				currentNode.parent.rightChild=None
		elif currentNode.hasBothChildren():
			succ=currentNode.findSuccessor()
			succ.spliceOut()
			currentNode.key=succ.key
			currentNode.payload=succ.payload
		else:
			if currentNode.hasLeftChild():
				if currentNode.isLeftChild():
					currentNode.leftChild.parent=currentNode.parent
					currentNode.parent.leftChild=currentNode.leftChild
				elif currentNode.isRightChild():
					currentNode.leftChild.parent=currentNode.parent
					currentNode.parent.rightChild=currentNode.leftChild
				else:
					currentNode.replaceNodeData(currentNode.leftChild.key,
												currentNode.leftChild.payload,
												currentNode.leftChild.leftChild,
												currentNode.leftChild.rightChild)
			else:
				if currentNode.isLeftChild():
					currentNode.rightChild.parent=currentNode.parent
					currentNode.parent.leftChild=currentNode.rightChild
				elif currentNode.isRightChild():
					currentNode.rightChild.parent=currentNode.parent
					currentNode.parent.rightChild=currentNode.rightChild
				else:
					currentNode.replaceNodeData(currentNode.rightChild.key,
												currentNode.rightChild.payload,
												currentNode.rightChild.leftChild,
												currentNode.rightChild.rightChild)

	def delete(self,key):
		if self.size>1:
			nodeToRemove=self._get(key,self.root)
			if nodeToRemove:
				self.remove(nodeToRemove)
				self.size=self.size-1
			else:
				raise KeyError('Error,key not in tree')
		elif self.size==1 and self.root.key==key:
			self.root=None
			self.size=self.size-1
		else:
			raise KeyError('Error,key not in tree')

	def inOrder(self):
		currentNode=self.root.findMin()
		while currentNode:
			print(currentNode.key,end=' ')
			currentNode=currentNode.findSuccessor()
		print()

class AVLTree(BinarySearchTree):
	def __init__(self):
		super().__init__()

	def rotateLeft(self,rotRoot):
		newRoot=rotRoot.rightChild
		rotRoot.rightChild=newRoot.leftChild
		if newRoot.leftChild!=None:
			newRoot.leftChild.parent=rotRoot
		newRoot.parent=rotRoot.parent
		if rotRoot.isRoot():
			self.root=newRoot
		else:
			if rotRoot.isLeftChild():
				rotRoot.parent.leftChild=newRoot
			else:
				rotRoot.parent.rightChild=newRoot
		newRoot.leftChild=rotRoot
		rotRoot.parent=newRoot
		rotRoot.balanceFactor=rotRoot.balanceFactor+1-min(newRoot.balanceFactor,0)
		newRoot.balanceFactor=newRoot.balanceFactor+1+max(rotRoot.balanceFactor,0)

	def rotateRight(self,rotRoot):
		newRoot=rotRoot.leftChild
		rotRoot.leftChild=newRoot.rightChild
		if newRoot.rightChild!=None:
			newRoot.rightChild.parent=rotRoot
		newRoot.parent=rotRoot.parent
		if rotRoot.isRoot():
			self.root=newRoot
		else:
			if rotRoot.isRightChild():
				rotRoot.parent.rightChild=newRoot
			else:
				rotRoot.parent.leftChild=newRoot
		newRoot.rightChild=rotRoot
		rotRoot.parent=newRoot
		rotRoot.balanceFactor=rotRoot.balanceFactor-1-max(newRoot.balanceFactor,0)
		newRoot.balanceFactor=newRoot.balanceFactor-1+min(rotRoot.balanceFactor,0)

	def rebalance(self,node):
		if node.balanceFactor<0:
			if node.rightChild.balanceFactor>0:
				self.rotateRight(node.rightChild)
				self.rotateLeft(node)
			else:
				self.rotateLeft(node)
		elif node.balanceFactor>0:
			if node.leftChild.balanceFactor<0:
				self.rotateLeft(node.leftChild)
				self.rotateRight(node)
			else:
				self.rotateRight(node)

	def updateBalance(self,node):
		if node.balanceFactor>1 or node.balanceFactor<-1:
			self.rebalance(node)
			return
		if node.parent!=None:
			if node.isLeftChild():
				node.parent.balanceFactor+=1
			elif node.isRightChild():
				node.parent.balanceFactor-=1

			if node.parent.balanceFactor!=0:
				self.updateBalance(node.parent)

	def _put(self,key,val,currentNode):
		if key<currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key,val,currentNode.leftChild)
			else:
				currentNode.leftChild=TreeNode(key,val,parent=currentNode)
				self.updateBalance(currentNode.leftChild)
		elif key>currentNode.key:
			if key==currentNode.key:
				key+=1
			if currentNode.hasRightChild():
				self._put(key,val,currentNode.rightChild)
			else:
				currentNode.rightChild=TreeNode(key,val,parent=currentNode)
				self.updateBalance(currentNode.rightChild)
		else:
			self._put(key+1,val,self.root)

		
class ThreadedBinaryTree(BinarySearchTree):
	def __init__(self):
		super().__init__()

	def updateTag(self):
		currentNode=self.root.findMin()
		nextNode=currentNode.findSuccessor()
		while True:	
			nextNode=currentNode.findSuccessor()
			if nextNode==None:
				break
			else:
				currentNode.rtag=nextNode
				nextNode.ltag=currentNode
				currentNode=nextNode

	def put(self,key,val):
		if self.root:
			self._put(key,val,self.root)
		else:
			self.root=TreeNode(key,val)
		self.size=self.size+1
		self.updateTag()

	def inOrder(self):
		currentNode=self.root.findMin()
		while currentNode:
			print(currentNode.payload,end=' ')
			currentNode=currentNode.rtag
		print()
bst=BinarySearchTree()
#bst=AVLTree()
#bst=ThreadedBinaryTree()
bst.put(17,17)
bst.put(5,5)
bst.put(2,2)
bst.put(16,16)
bst.put(35,35)
bst.put(29,29)
bst.put(38,38)
bst.put(33,33)
bst.put(19,19)
bst.put(18,18)
bst.put(18,18)
bst.inOrder()
#for x in bst:
#	print(x,end=' ')
#print()
#r=bst.root
#print(17 in bst)
#bst.delete(17)
#for x in bst:
#	print(x,end=' ')
#print()





