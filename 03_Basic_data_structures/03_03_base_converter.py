from pythonds.basic import Stack

def divideBy2(decNumber):
	remstack=Stack()

	while decNumber>0:
		rem=decNumber%2
		remstack.push(rem)
		decNumber=decNumber//2

	binString=""
	while not remstack.isEmpty():
		binString=binString+str(remstack.pop())

	return binString

def baseConverter(decNumber,base):
	digits='0123456789ABCDEF'

	remstack=Stack()

	while decNumber>0:
		rem=decNumber%base
		remstack.push(rem)
		decNumber=decNumber//base

	newString=""
	while not remstack.isEmpty():
		newString=newString+digits[remstack.pop()]

	return newString

print(divideBy2(1024))
print(baseConverter(1024,2))
print(baseConverter(1024,8))
print(baseConverter(1024,10))
print(baseConverter(1024,16))
print(baseConverter(1034,16))

