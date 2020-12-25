class ArrayList:
	def __init__(self):
		self.sizeExponent=-1
		self.maxSize=0
		self.lastIndex=0
		self.myArray=[]

	def __getitem__(self,idx):
		if idx<self.lastIndex:
			return self.myArray[idx]
		else:
			raise LookupError('index out of bounds')

	def __setitem__(self,idx,val):
		if idx<self.lastIndex:
			self.myArray[idx]=val
		else:
			raise LookupError('index out of bounds')

	def __add__(self,other):
		addAL=ArrayList()
		for self_elem in self.myArray[0:self.lastIndex]:
			addAL.append(self_elem)
		for other_elem in other.myArray[0:other.lastIndex]:
			addAL.append(other_elem)
		return addAL

	def __mul__(self,num):
		if type(num)!=int:
			print("error")
		else:
			mulAL=ArrayList()
			for i in range(num):
				for elem in self.myArray[0:self.lastIndex]:
					mulAL.append(elem)
			return mulAL



	def __resize(self):
		self.sizeExponent+=1
		newsize=2**self.sizeExponent
		newarray=[0]*newsize
		for i in range(self.maxSize):
			newarray[i]=self.myArray[i]
		self.maxSize=newsize
		self.myArray=newarray

	def __desize(self):
		self.sizeExponent-=1
		newsize=2**self.sizeExponent
		self.maxSize=newsize
		newarray=[0]*newsize
		for i in range(self.maxSize):
			newarray[i]=self.myArray[i]		
		self.myArray=newarray

	def append(self,val):
		if self.lastIndex>self.maxSize-1:
			self.__resize()

		self.myArray[self.lastIndex]=val
		self.lastIndex+=1

	def insert(self,idx,val):
		if self.lastIndex>self.maxSize-1:
			self.__resize()
		for i in range(self.lastIndex,idx-1,-1):
			self.myArray[i+1]=self.myArray[i]
		self.lastIndex+=1
		self.myArray[idx]=val

	def pop(self,idx=None):
		if not idx:
			idx=self.lastIndex-1
		if idx<self.lastIndex:
			self.lastIndex-=1
			elem=self.myArray.pop(idx)
			self.myArray.append(0)
		else:
			raise LookupError('index out of bounds')
		if (self.lastIndex-1)*2<self.maxSize:
			self.__desize()
		return elem

	def delete(self,idx):
		if idx<self.lastIndex:
			self.lastIndex-=1
			elem=self.myArray.pop(idx)
			self.myArray.append(0)
		else:
			raise LookupError('index out of bounds')
		
		if (self.lastIndex-1)*2<self.maxSize:
			self.__desize()
		return elem

	def index(self,val):
		exist=False
		for idx in range(self.lastIndex):
			if self.myArray[idx]==val:
				exist=True
				break

		if exist:
			return idx
		else:
			print(str(val)+" not found!")

al=ArrayList()
al.append(0)
al.append(1)
al.append(2)
al.append(3)
for i in range(al.lastIndex):
	print(al[i],end=' ')
print()
al[0]=10
al[3]=100
print(al.myArray)
al.insert(1,10)
print(al.myArray)
al.delete(1)
print(al.myArray)
al.pop()
print(al.myArray)
print(al.index(10))

al2=ArrayList()
al2.append(4)
al2.append(5)
al2.append(6)
al3=al+al2
print(al3.myArray)
al4=al*3
print(al4.myArray)
