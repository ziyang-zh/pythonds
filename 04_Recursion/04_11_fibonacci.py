def fabonacci(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fabonacci(n-1)+fabonacci(n-2)

print(fabonacci(0))
print(fabonacci(1))
print(fabonacci(2))
print(fabonacci(5))
print(fabonacci(8))
