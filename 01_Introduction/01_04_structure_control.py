#structure control
#while
counter=1
while counter<3:
	print("Hello world")
	counter=counter+1

for item in [1,3,6,2,5]:
	print(item)

for item in range(5):
	print(item*2)

wordlist=['cat','dog','rabbit']
letterlist=[]
for aword in wordlist:
	for aletter in aword:
		letterlist.append(aletter)
print(letterlist)

#if
import math
n=-4
if n<0:
	n=abs(n)
	print(math.sqrt(n))
else:
	print(math.sqrt(n))

score=99
if score>=90:
	print("A")
else:
	if score>=80:
		print("B")
	else:
		if score>=70:
			print("C")
		else:
			if score>=60:
				print("D")
			else:
				print("F")

#else if
if score>=90:
	print("A")
elif score>=80:
	print("B")
elif score>=70:
	print("C")
elif score>=60:
	print("D")
else:
	print("F")

#for
sqlist=[]
for x in range(1,11):
	sqlist.append(x*x)
print(sqlist)

sqlist=[x*x for x in range(1,11)]
print(sqlist)