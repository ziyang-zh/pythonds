def selectionSort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax=0
		for location in range(1,fillslot+1):
			if alist[location]>alist[positionOfMax]:
				positionOfMax=location

		alist[fillslot],alist[positionOfMax]=alist[positionOfMax],alist[fillslot]
	return alist

ls=[2,4,2,1,2,3,1,9]
print(ls)
selectionSort(ls)
print(ls)
