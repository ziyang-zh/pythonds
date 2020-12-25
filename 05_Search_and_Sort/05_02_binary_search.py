def binarySearch(alist,item):
	first=0
	last=len(alist)-1
	found=False

	while first<=last and not found:
		midpoint=(first+last)//2
		if alist[midpoint]==item:
			found=True
		else:
			if item<alist[midpoint]:
				last=midpoint-1
			else:
				first=midpoint+1

	return found

def binarySearch_rec(alist,item):
	if len(alist)==0:
		return False
	else:
		midpoint=len(alist)//2
		if alist[midpoint]==item:
			return True
		else:
			if item<alist[midpoint]:
				return binarySearch_rec(alist[:midpoint],item)
			else:
				return binarySearch_rec(alist[midpoint+1:],item)

ols=[1,2,3,4,5]
print(binarySearch(ols,3))
print(binarySearch(ols,6))
print(binarySearch_rec(ols,3))
print(binarySearch_rec(ols,6))
