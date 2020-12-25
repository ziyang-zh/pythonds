from timeit import Timer

def test1():
	l=[]
	for i in range(1000):
		l=l+[i]

def test2():
	l=[]
	for i in range(1000):
		l.append(i)

def test3():
	l=[i for i in range(1000)]

def test4():
	l=list(range(1000))

t1=Timer("test1()","from __main__ import test1")
print("concat",t1.timeit(number=1000),"milliseconds")

t2=Timer("test2()","from __main__ import test2")
print("append",t2.timeit(number=1000),"milliseconds")

t3=Timer("test3()","from __main__ import test3")
print("comprehension",t3.timeit(number=1000),"milliseconds")

t4=Timer("test4()","from __main__ import test4")
print("list range ",t4.timeit(number=1000),"milliseconds")

popzero=Timer("x.pop(0)","from __main__ import x")
popend=Timer("x.pop()","from __main__ import x")
print("pop(0) pop()")
for i in range(100000,1000001,100000):
	x=list(range(i))
	pt=popzero.timeit(number=1000)
	x=list(range(i))
	pz=popend.timeit(number=1000)
	print("%15.5f, %15.5f" % (pz,pt))
