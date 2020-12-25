class HashTble:
	def __init__(self):
		self.size=11
		self.slots=[None]*self.size
		self.data=[None]*self.size
		self.count=0

	def __len__(self):
		return self.count

	def __contains__(self,item):
		if item:
			return item in self.data


	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,data):
		self.put(key,data)

	def __delitem__(self,key):
		idx=self.slots.index(key)
		self.slots[idx]=None
		self.data[idx]=None

	def hashfunction(self,key,size):
		return key%size

	def rehash(self,oldhash,size):
		return (oldhash+1)%size

	def put(self,key,data):
		hashvalue=self.hashfunction(key,len(self.slots))

		if self.slots[hashvalue]==None:
			self.slots[hashvalue]=key
			self.data[hashvalue]=data
			self.count+=1
		else:
			if self.slots[hashvalue]==key:
				self.data[hashvalue]=data
			else:
				nextslot=self.rehash(hashvalue,len(self.slots))
				while self.slots[nextslot]!=None and self.slots[nextslot]!=key:
					nextslot=self.rehash(nextslot,len(self.slots))

				if self.slots[nextslot]==None:
					self.slots[nextslot]=key
					self.data[nextslot]=data
					self.count+=1
				else:
					self.data[nextslot]=data

	def get(self,key):
		startslot=self.hashfunction(key,len(self.slots))

		data=None
		stop=False
		found=False
		position=startslot
		while self.slots[position]!=None and not found and not stop:
			if self.slots[position]==key:
				found=True
				data=self.data[position]
			else:
				position=self.rehash(position,len(self.slots))
				if position==startslot:
					stop=True
		return data

H=HashTble()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
print(H[20])
print(H[17])
H[20]="duck"
print(H[20])
print(H.data)
print(len(H))
print("duck" in H)
print("chicken" in H)
del H[54]
print(H.data)

	




