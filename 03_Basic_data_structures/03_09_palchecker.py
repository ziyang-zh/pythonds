from pythonds.basic import Deque
def palchecker(aString):
	chardeque=Deque()

	for ch in aString:
		if ch!=' ':
			chardeque.addRear(ch)

	stillEqual=True

	while chardeque.size()>1 and stillEqual:
		first=chardeque.removeFront()
		last=chardeque.removeRear()
		if first!=last:
			stillEqual=False

	return stillEqual

print(palchecker("abccba"))
print(palchecker("abcba"))
print(palchecker("abc"))
print(palchecker("I PREFER PI"))