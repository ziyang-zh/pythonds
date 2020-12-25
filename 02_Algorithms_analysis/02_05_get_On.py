from timeit import Timer
import random
import numpy as np
from matplotlib import pyplot as plt 

x=[]
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
listindex=Timer("l[200]","from __main__ import l")
dictgetvalue=Timer("d[200]","from __main__ import d")
dictsetvalue=Timer("d[200]=0","from __main__ import d")
listdel=Timer("del l[200]","from __main__ import l")
dictdel=Timer("d[200]","from __main__ import d")
for i in range(10000,1000001,10000):
	x.append(i)
	l=list(range(i))
	d={k:None for k in range(i)}

	t1=listindex.timeit(1000)
	t2=dictgetvalue.timeit(1000)
	t3=dictsetvalue.timeit(1000)
	t4=listdel.timeit(1000)
	t5=dictdel.timeit(1000)

	y1.append(t1)
	y2.append(t2)
	y3.append(t3)
	y4.append(t4)
	y5.append(t5)

plt.figure(figsize=(100,20))
plt.plot(x,y1,'r.-',linewidth=2,ms=5)
plt.plot(x,y2,'g.-',linewidth=2,ms=5)
plt.plot(x,y3,'b.-',linewidth=2,ms=5)
#plt.plot(x,y4,'y.-',linewidth=2,ms=5)
plt.plot(x,y5,'burlywood.-',linewidth=2,ms=5)
my_x_ticks=np.arange(x[0],x[-1],10000)
plt.xticks(my_x_ticks)
plt.show()