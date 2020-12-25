def reverseList(alist,start,end):
	if start==end:
		return alist
	else:
		temp=alist[start]
		alist[start]=alist[end-1]
		alist[end-1]=temp
		alist=reverseList(alist,start+1,end-1)
		return alist

ls=[0,1,2,3,4,5,6,7]
ls_rever=reverseList(ls,0,len(ls))
print(ls_rever)
