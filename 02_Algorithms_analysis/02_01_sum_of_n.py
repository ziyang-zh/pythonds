import time
def sumOfN(n):
	theSum=0
	for i in range(1,n+1):
		theSum=theSum+i
	return theSum

for i in range(5):
	print("Sum is %d " % sumOfN(10000))

def sumOfN2(n):
	start=time.time()
	theSum=0
	for i in range(1,n+1):
		theSum=theSum+i
	end=time.time()
	return theSum,end-start

for i in range(5):
	print("Sum is %d required %10.7f seconds" % sumOfN2(10000))
for i in range(5):
	print("Sum is %d required %10.7f seconds" % sumOfN2(100000))

def sumOfN3(n):
	theSum=(n*(n+1))/2
	return theSum

for i in range(5):
	print("Sum is %d required %10.7f seconds" % sumOfN2(10000*10**i))