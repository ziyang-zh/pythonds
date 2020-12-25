def pascal(ls=[]):
	if ls==[]:
		return [1]
	else:
		temp=[]
		for i in range(len(ls)+1):
			if i==0 or i==len(ls):
				temp.append(1)
			else:
				temp.append(ls[i-1]+ls[i])
		return temp

def pascalTriangle(n,ls=[]):
	if n>0:
		ls=pascal(ls)
		print(' '*n,end='')
		for i in range(len(ls)):
			print(ls[i],end=' ')
		print()
		pascalTriangle(n-1,ls)

pascalTriangle(8)