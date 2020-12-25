def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				alist[i],alist[i+1]=alist[i+1],alist[i]
	return alist

def shortBubbleSort(alist):
	exchanges=True
	passnum=len(alist)-1
	while passnum>0 and exchanges:
		exchanges=False
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				exchanges=True
				alist[i],alist[i+1]=alist[i+1],alist[i]
		passnum=passnum-1
	return alist

def doubleBubbleSort(alist):
	rank=1
	head=0
	tail=len(alist)-1
	exchanges=True
	while head<tail and exchanges:
		exchanges=False
		if rank%2:
			for i in range(head,tail-1):
				if alist[i]>alist[i+1]:
					exchanges=True
					alist[i],alist[i+1]=alist[i+1],alist[i]
			tail-=1
		else:
			for i in range(tail-1,head,-1):
				if alist[i]<alist[i-1]:
					exchanges=True
					alist[i],alist[i-1]=alist[i-1],alist[i]
			head+=1
		rank+=1
		
	return alist

ls=[2,4,2,1,2,3,1,9]
print(ls)
bubbleSort(ls)
print(ls)

ls=[2,4,2,1,2,3,1,9]
print(ls)
shortBubbleSort(ls)
print(ls)

ls=[2,4,2,1,2,3,1,9]
print(ls)
doubleBubbleSort(ls)
print(ls)
