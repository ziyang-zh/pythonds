from pythonds.basic import Stack

def maches(open,close):
	opens="([{"
	closers=")]}"

	return opens.index(open)==closers.index(close)

def parChecker(symbolString):
	s=Stack()
	
	balanced=True
	index=0

	while index<len(symbolString) and balanced:
		symbol=symbolString[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced=False
			else:
				top=s.pop()
				if not maches(top,symbol):
					balanced=False

		index=index+1

	if balanced and s.isEmpty():
		return True
	else:
		return False

print(parChecker('(()()())'))
print(parChecker('(((())))'))
print(parChecker('(()((()())))'))

print(parChecker('((((((())'))
print(parChecker('()))'))
print(parChecker('(()()(()'))

print(parChecker('{{([][])}()}'))
print(parChecker('[[{{(())}}]]'))
print(parChecker('[][][](){}'))

print(parChecker('([)]'))
print(parChecker('((()]))'))
print(parChecker('[{()]'))