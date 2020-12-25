class BinaryHeap:
	def __init__(self):
		self.heapList=[0]
		self.currentSize=0
		self.maxSize=3

	def perUp(self,i):
		while i//2>0:
			if self.heapList[i]<self.heapList[i//2]:
				self.heapList[i],self.heapList[i//2]=self.heapList[i//2],self.heapList[i]
			i//=2

	def minChild(self,i):
		if i*2+1>self.currentSize:
			return i*2
		else:
			if self.heapList[i*2]<self.heapList[i*2+1]:
				return i*2
			else:
				return i*2+1

	def perDown(self,i):
		while (i*2)<=self.currentSize:
			mc=self.minChild(i)
			if self.heapList[i]>self.heapList[mc]:
				self.heapList[i],self.heapList[mc]=self.heapList[mc],self.heapList[i]
			i=mc

	def insert(self,k):
		if self.currentSize==self.currentSize:
			self.heapList.pop()
		self.heapList.append(k)
		self.currentSize+=1
		self.perUp(self.currentSize)

	def delMin(self):
		retral=self.heapList[1]
		self.heapList[1]=self.heapList[self.currentSize]
		self.currentSize-=1
		self.heapList.pop()
		self.perDown(1)
		return retral

	def buildHeap(self,alist):
		for k in range(len(alist)-self.maxSize):
			alist.pop(alist.index(max(alist))) 
		self.currentSize=len(alist)
		self.heapList=[0]+alist[:]
		i=len(alist)//2
		while i>0:
			self.perDown(i)
			i-=1

bh=BinaryHeap()
bh.buildHeap([9,6,5,3,3])
print(bh.delMin())
print(bh.heapList)



