from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator

def buildParseTree(fpexp):
	fpexp=fpexp.replace(' ','')
	fplist=[]
	i=0
	while i<len(fpexp):
		if fpexp[i]=='a':
			fplist.append('and')
			i+=3
		elif fpexp[i]=='o':
			fplist.append('or')
			i+=2
		elif fpexp[i]=='n':
			fplist.append('not')
			i+=3
		else:
			fplist.append(fpexp[i])
			i+=1

	pStack=Stack()
	eTree=BinaryTree('')
	pStack.push(eTree)
	currentTree=eTree
	j=0
	while j<len(fplist):
		i=fplist[j]
		if i=='(' and fplist[j+1]=='not':
			currentTree.setRootVal('not')
			currentTree.insertRight('')
			pStack.push(currentTree)
			currentTree=currentTree.getRightChild()
			j+=1
		elif i=='(':
			currentTree.insertLeft('')
			pStack.push(currentTree)
			currentTree=currentTree.getLeftChild()
		elif i not in '+-*/)andor':
			currentTree.setRootVal(eval(i))
			parent=pStack.pop()
			currentTree=parent
		elif i in '+-*/andor':
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			pStack.push(currentTree)
			currentTree=currentTree.getRightChild()
		elif i==')':
			currentTree=pStack.pop()
		else:
			raise ValueError("Unknown Operator: "+i)
		j+=1
	return eTree
	
def printexp(tree):
	sVal=""
	if tree:
		if str(tree.getRootVal()) not in '+-*/)andornot':
			sVal=printexp(tree.getLeftChild())
			sVal=sVal+str(tree.getRootVal())
			sVal=sVal+printexp(tree.getRightChild())
		else:
			sVal='('+printexp(tree.getLeftChild())
			sVal=sVal+str(tree.getRootVal())
			sVal=sVal+printexp(tree.getRightChild())+')'
	return sVal

def operator_and(x,y):
	return bool(x) and bool(y)

def operator_or(x,y):
	return bool(x) or bool(y)

def operator_not(x):
	return not bool(x)

def evaluate(parseTree):
	opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv,
			'and':operator_and,'or':operator_or,'not':operator_not}
	leftC=parseTree.getLeftChild()
	rightC=parseTree.getRightChild()

	if leftC and rightC:
		fn=opers[parseTree.getRootVal()]
		return fn(evaluate(leftC),evaluate(rightC))
	elif rightC:
		fn=opers[parseTree.getRootVal()]
		return fn(evaluate(rightC))
	else:
		return parseTree.getRootVal()

def postordereval(tree):
	opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv,
			'and':operator_and,'or':operator_or,'not':operator_not}
	res1=None
	res2=None
	if tree:
		res1=postordereval(tree.getLeftChild())
		res2=postordereval(tree.getRightChild())
		if res1 and res2:
			return opers[tree.getRootVal()](res1,res2)
		else:
			return tree.getRootVal()

exp='(3+(4*5))'
pt=buildParseTree(exp)
print(printexp(pt))
print(evaluate(pt))
print(postordereval(pt))

exp='(not((1 and 0) or 0))'
pt=buildParseTree(exp)
print(printexp(pt))
print(evaluate(pt))