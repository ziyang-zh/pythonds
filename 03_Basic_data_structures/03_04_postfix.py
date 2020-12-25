from pythonds.basic import Stack
from pythonds.basic import Queue

def isNumber(token):
	flag=True
	for i in range(len(token)):
		if token[i] not in "0123456789":
			flag=False
	return flag

def isOperator(token):
	flag=True
	for i in range(len(token)):
		if token[i] not in "+-*/^%":
			flag=False
	return flag

def isPar(token):
	flag=False
	if token in "([{<":
		flag=1
	elif token in ")]}>":
		flag=2
	return flag

def parMaches(open,close):
	opens="([{<"
	closers=")]}>"
	return opens.index(open)==closers.index(close)

def parChecker(symbolString):
	pars=[]
	for token in symbolString:
		if isPar(token):
			pars.append(token)

	s=Stack()
	flag=True
	index=0
	while index<len(pars) and flag:
		par=pars[index]
		if isPar(par)==1:
			s.push(par)
		elif isPar(par)==2:
			if s.isEmpty():
				flag=False
			else:
				top=s.pop()
				if not parMaches(top,par):
					flag=False
		index=index+1

	if flag and s.isEmpty():
		return True
	else:
		return False

def isLegal(symbolString):
	flag=True
	for token in symbolString.replace(' ',''):
		if not (isNumber(token) or isOperator(token) or isPar(token)):
			flag=False
			print("INOUT ILLEGAL!("+token+")")

	if not parChecker(symbolString):
		flag=False
		print("BRACKET DISMATCH！")
	return flag

def doMath(op,op1,op2):
	if op=="*":
		return op1*op2
	elif op=="/":
		return op1/op2
	elif op=="+":
		return op1+op2
	elif op=="-":
		return op1-op2
	elif op=="%":
		return op1%op2
	elif op=="^":
		return op1**op2

def infixToPostfix(infixexpr):
	tokenList=list(infixexpr.replace(' ',''))
	prec={'^':4,'%':3,'*':3,'/':3,'+':2,'-':2,'(':1,'[':1,'{':1,'<':1}
	numQueue=Queue()
	opStark=Stack()
	postfixList=[]
	
	tokenList_tmp=[]
	for token in tokenList:
		if isNumber(token):
			numQueue.enqueue(token)
		else:
		 	if numQueue.isEmpty():
		 		tokenList_tmp.append(token)
		 	else:
		 		num=''
		 		for i in range(numQueue.size()):
		 			num+=numQueue.dequeue()
		 		tokenList_tmp.append(num)
		 		tokenList_tmp.append(token)
	
	if not numQueue.isEmpty():
		num=''
		for i in range(numQueue.size()):
			num+=numQueue.dequeue()
		tokenList_tmp.append(num)	 		
	
	tokenList=tokenList_tmp

	for token in tokenList:
		if isNumber(token):
			postfixList.append(token)
		elif isPar(token)==1:
			opStark.push(token)
		elif isPar(token)==2:
			topToken=opStark.pop()
			while isPar(topToken)!=1:
				postfixList.append(topToken)
				topToken=opStark.pop()
		else:
			while (not opStark.isEmpty()) and \
				(prec[opStark.peek()]>=prec[token]):
				postfixList.append(opStark.pop())
			opStark.push(token)

	while not opStark.isEmpty():
		postfixList.append(opStark.pop())
	return postfixList

def postfixEval(postfixList):
	tokenList=postfixList
	operandStack=Stack()
	
	for token in tokenList:
		if isNumber(token):
			operandStack.push(int(token))
		else:
			operand2=operandStack.pop()
			operand1=operandStack.pop()
			result=doMath(token,operand1,operand2)
			operandStack.push(result)

	return operandStack.pop()

def infixComputer(infixexpr):
	if not isLegal(infixexpr):
		print(end='')
	else:
		print(infixexpr+" = ",end="")
		postfixList=infixToPostfix(infixexpr)
		result=postfixEval(postfixList)
		print(result)

infixComputer("(12+4%2)*(3+4)")
infixComputer("( 1 + 101 ) * 3")
infixComputer("1 + 288 * 3")
infixComputer("1 + 288 * 3)")
infixComputer("1 + 288 * 3)_")
