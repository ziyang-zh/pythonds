from timeit import Timer
import random
import numpy as np
from matplotlib import pyplot as plt 

x=[]
y1=[]
y2=[]
listdel=Timer("del l[100]","from __main__ import l")
dictdel=Timer("del d[100]","from __main__ import d")
for i in range(10000,100001,2000):
	x.append(i)
	l=list(range(i))
	d={k:k for k in range(i)}

	t1=listdel.timeit(1)
	t2=dictdel.timeit(1)
	y1.append(t1)
	y2.append(t2)

plt.figure(figsize=(100,20))
plt.plot(x,y1,'r.-',linewidth=2,ms=5)
plt.plot(x,y2,'g.-',linewidth=2,ms=5)
my_x_ticks=np.arange(x[0],x[-1],2000)
plt.xticks(my_x_ticks)
plt.show()