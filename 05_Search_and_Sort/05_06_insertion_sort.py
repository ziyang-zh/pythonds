def insertionSort(alist):
	for index in range(1,len(alist)):
		currentvalue=alist[index]
		position=index

		while position>0 and alist[position-1]>currentvalue:
			alist[position]=alist[position-1]
			position=position-1

		alist[position]=currentvalue
	return alist

ls=[2,4,2,1,2,3,1,9]
print(ls)
insertionSort(ls)
print(ls)
