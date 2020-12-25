from pythonds.basic import Stack

rStack=Stack()
def toStr(n,base):
	
	convertString='0123456789ABCDEF'

	if n<base:
		rStack.push(convertString[n])
	else:
		rStack.push(convertString[n%base])
		toStr(n//base,base)



toStr(11,2)
for i in range(rStack.size()):
	print(rStack.pop(),end='')
print()