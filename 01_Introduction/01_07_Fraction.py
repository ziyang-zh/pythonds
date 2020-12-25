
class Fraction:
	
	def __init__(self,top,bottom):
		if isinstance(top,int) and isinstance(bottom,int):
			if bottom==0:
				raise RuntimeError("Error: DENOMINATOR EQUAL 0!")
			elif bottom<0:
				bottom=-bottom
				top=-top

			common=self.gratest_common_divisor(top,bottom)
			self.num=top//common
			self.den=bottom//common

		else:
			raise RuntimeError("Error: Numerator or Denominator is not a Integer!")

	def __str__(self):
		return str(self.num)+"/"+str(self.den)

	def __repr__(self):
		return str(self.num)+"/"+str(self.den)

	def __add__(self,other):
		newnum=self.num*other.den+self.den*other.num
		newden=self.den*other.den

		return Fraction(newnum,newden)

	def __sub__(self,other):
		newnum=self.num*other.den-self.den*other.num
		newden=self.den*other.den

		return Fraction(newnum,newden)

	def __mul__(self,other):
		newnum=self.num*other.num
		newden=self.den*other.den

		return Fraction(newnum,newden)

	def __truediv__(self,other):
		newnum=self.num*other.den
		newden=self.den*other.num

		return Fraction(newnum,newden)

	def __eq__(self,other):
		firstnum=self.num*other.den
		secondnum=self.den*other.num
		return firstnum==secondnum

	def __gt__(self,other):
		firstnum=self.num*other.den
		secondnum=self.den*other.num
		return firstnum>secondnum

	def __ge__(self,other):
		firstnum=self.num*other.den
		secondnum=self.den*other.num
		return firstnum>=secondnum

	def __lt__(self,other):
		firstnum=self.num*other.den
		secondnum=self.den*other.num
		return firstnum<secondnum

	def __le__(self,other):
		firstnum=self.num*other.den
		secondnum=self.den*other.num
		return firstnum<=secondnum

	def __ne__(self,other):
		firstnum=self.num*other.den
		secondnum=self.den*other.num
		return firstnum!=secondnum

	def __radd__(self,other):
		newnum=self.num*other.den+self.den*other.num
		newden=self.den*other.den
		return Fraction(newnum,newden)

	def __iadd__(self,other):
		newnum=self.num*other.den+self.den*other.num
		newden=self.den*other.den
		return Fraction(newnum,newden)

	def show(self):
		print(self.num,"/",self.den,sep='')

	def getNum(self):
		return self.num

	def getDen(self):
		return self.den

	def gratest_common_divisor(self,m,n):
		while m%n != 0:
			oldm=m
			oldn=n

			m=oldn
			n=oldm%oldn
		return n

myfraction=Fraction(3,5)
print("myfraction is: ",end='')
print(myfraction)
print("myfraction is: "+myfraction.__str__())
print("myfraction is: "+myfraction.__repr__())
print("myfraction is: "+str(myfraction))
print("myfraction is: ",end='')
myfraction.show()
print()

print("numerator is:   "+str(myfraction.getNum()))
print("denominator is: "+str(myfraction.getDen()))
print()

f1=Fraction(1,3)
f2=Fraction(3,5)

print(str(f1)+" + "+str(f2)+" = "+str(f1+f2))
print(str(f1)+" - "+str(f2)+" = "+str(f1-f2))
print(str(f1)+" * "+str(f2)+" = "+str(f1*f2))
print(str(f1)+" / "+str(f2)+" = "+str(f1/f2))
print()

print(str(f1)+" = "+str(f2)+" ? "+str(f1==f2))
print(str(f1)+" > "+str(f2)+" ? "+str(f1>f2))
print(str(f1)+" >= "+str(f2)+" ? "+str(f1>=f2))
print(str(f1)+" < "+str(f2)+" ? "+str(f1<f2))
print(str(f1)+" <= "+str(f2)+" ? "+str(f1<=f2))
print(str(f1)+" != "+str(f2)+" ? "+str(f1!=f2))
print()

print(str(f1)+" = "+str(f1)+" ? "+str(f1==f1))
print(str(f1)+" > "+str(f1)+" ? "+str(f1>f1))
print(str(f1)+" >= "+str(f1)+" ? "+str(f1>=f1))
print(str(f1)+" < "+str(f1)+" ? "+str(f1<f1))
print(str(f1)+" <= "+str(f1)+" ? "+str(f1<=f1))
print(str(f1)+" != "+str(f1)+" ? "+str(f1!=f1))
print()

#f3=Fraction(0.5,1)
#f4=Fraction(3,0)
f3=Fraction(1,2)
f4=Fraction(3,-4)
print(str(f3)+" + "+str(f4)+" = "+str(f3+f4))
print(str(f3)+" - "+str(f4)+" = "+str(f3-f4))
print(str(f3)+" * "+str(f4)+" = "+str(f3*f4))
print(str(f3)+" / "+str(f4)+" = "+str(f3/f4))
print()

print(f1)
f1+=f2
print(f2)
