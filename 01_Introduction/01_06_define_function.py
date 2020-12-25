#define function
def square(n):
	return n**2

print(square(3))
print(square(square(3)))

#Newton-Raphson method
def squareroot(n):
	root=n/2
	for i in range(20):
		root=1/2*(root+n/root)
	
	return root

print(squareroot(9))
print(squareroot(4563))