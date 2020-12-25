def mergeSort(alist):
	print("splitting ",alist)
	if len(alist)>1:
		mid=len(alist)//2
		lefthalf=[]
		righthalf=[]
		for i in range(mid):
			lefthalf.append(alist[i])
		for j in range(mid,len(alist)):
			righthalf.append(alist[j])
		print(lefthalf,righthalf)

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i=0
		j=0
		k=0
		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i]<righthalf[j]:
				alist[k]=lefthalf[i]
				i=i+1
			else:
				alist[k]=righthalf[j]
				j=j+1
			k=k+1
		
		while i<len(lefthalf):
			alist[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j<len(righthalf):
			alist[k]=righthalf[j]
			j=j+1
			k=k+1
	print("merging ",alist)

b=[54,26,93,17,77,31,44,55,20]
mergeSort(b)
