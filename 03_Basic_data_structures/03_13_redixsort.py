from pythonds.basic import Queue
def getFigure(number):
	figure=0
	while number!=0:
		number//=10
		figure+=1
	return figure

def getRedix(number,digit):
	for i in range(digit):
		number//=10
	return number%10

def redixSort(numberlist):
	buckets=[Queue() for i in range(10)]
	maximum=max(numberlist)
	maxFigure=getFigure(maximum)


	for digit in range(maxFigure):
		for number in numberlist:
			redix=getRedix(number,digit)
			buckets[redix].enqueue(number)

		new_numberlist=[]
		for bucket in buckets:
			while not bucket.isEmpty():
				new_numberlist.append(bucket.dequeue())
		numberlist=new_numberlist
	return numberlist

numberlist=[102,1,998,0,22,48,58,49,333,632131213]
numberlist_sorted=redixSort(numberlist)
print(numberlist_sorted)

