def shellSort(alist):
	sublistcount=len(alist)//2
	while sublistcount>0:
		for startposition in range(sublistcount):
			gapInsertionSort(alist,startposition,sublistcount)

		print("After increments of size",sublistcount,"The list is",alist)
		sublistcount=sublistcount//2

def gapInsertionSort(alist,start,gap):
	for i in range(start+gap,len(alist),gap):
		currentvalue=alist[i]
		position=i
		while position>=gap and alist[position-gap]>currentvalue:
			alist[position]=alist[position-gap]
			position=position-gap
		alist[position]=currentvalue


ls=[2,4,2,1,2,3,1,9]
print(ls)
shellSort(ls)
print(ls)