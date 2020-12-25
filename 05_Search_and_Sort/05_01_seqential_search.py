def sequentialSearch(alist,item):
	pos=0
	found=False

	while pos <len(alist) and not found:
		if alist[pos]==item:
			found=True
		else:
			pos=pos+1

	return found
ls=[1,4,2,3,0]
print(sequentialSearch(ls,4))
print(sequentialSearch(ls,5))

def orderedSerquentialSearch(alist,item):
	pos=0
	found=False
	stop=False
	while pos <len(alist) and not found and not stop:
		if alist[pos]==item:
			found=True
		else:
			if alist[pos]>item:
				stop=True
			else:
				pos=pos+1
	return found

ols=[1,2,3,4,5]
print(orderedSerquentialSearch(ols,3))
print(orderedSerquentialSearch(ols,6))
