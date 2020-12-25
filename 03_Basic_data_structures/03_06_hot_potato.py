from pythonds.basic import Queue

def hotPotato(namelist,num):
	simqueue=Queue()
	for name in namelist:
		simqueue.enqueue(name)

	while simqueue.size()>1:
		for i in range(1,num):
			simqueue.enqueue(simqueue.dequeue())

		out=simqueue.dequeue()
		print(out)

	return simqueue.dequeue()

print(hotPotato(["bill","David","Susan","Jane","Kent","Brad"],7))