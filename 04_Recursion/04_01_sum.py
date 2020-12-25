numlist=[0,1,2,3,4,5,6,7,8,9]

def listsum(numList):
	theSum=0
	for i in numList:
		theSum=theSum+i
	return theSum

print(listsum(numlist))

def listsum(numList):
	if len(numList) ==1:
		return numList[0]
	else:
		return numList[0] + listsum(numList[1:])

print(listsum(numlist))
