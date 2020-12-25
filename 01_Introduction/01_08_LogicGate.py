class LogicGate:
	def __init__(self,n):
		self.label=n
		self.output=None

	def getLabel(self):
		return self.label

	def getOutput(self):
		self.output=self.performGateLogic()
		return self.output

class BinaryGate(LogicGate):
	def __init__(self,n):
		super().__init__(n)
		self.pinA=None
		self.pinB=None

	def setPin(self,pin):
		if self.pinA==None:
			self.pinA=pin
		elif self.pinB==None:
			self.pinB=pin
		else:
			raise RuntimeError("Error: NO EMPTY PINS")

	def getPinA(self):
		if self.pinA==0 or self.pinA==1:
			return self.pinA
		else:
			return self.pinA.getFrom().getOutput()

	def getPinB(self):
		if self.pinB==0 or self.pinB==1:
			return self.pinB
		else:
			return self.pinB.getFrom().getOutput()

	def setNextPin(self,source):
		if self.pinA==None:
			self.pinA=source
		elif self.pinB==None:
			self.pinB=source
		else:
			raise RuntimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):
	def __init__(self,n):
		super().__init__(n)
		self.pin=None
	
	def setPin(self,pin):
		if self.pin==None:
			self.pin=pin
		else:
			raise RuntimeError("Error: NO EMPTY PINS")

	def getPin(self):
		if self.pin==None:
			return self.pin
		else:
			return self.pin.getFrom().getOutput()

	def setNextPin(self,source):
		if self.pin==None:
			self.pin=source
		else:
			raise RuntimeError("Error: NO EMPTY PINS")

class AndGate(BinaryGate):
	def __init__(self,n):
		super().__init__(n)

	def performGateLogic(self):
		a=self.getPinA()
		b=self.getPinB()
		if a==1 and b==1:
			return 1
		else:
			return 0

class OrGate(BinaryGate):
	def __init__(self,n):
		super().__init__(n)

	def performGateLogic(self):
		a=self.getPinA()
		b=self.getPinB()
		if a==1 or b==1:
			return 1
		else:
			return 0

class NotGate(UnaryGate):
	def __init__(self,n):
		super().__init__(n)

	def performGateLogic(self):
		o=self.getPin()
		if o==0:
			return 1
		else:
			return 0

class NandGate(BinaryGate):
	def __init__(self,n):
		super().__init__(n)

	def performGateLogic(self):
		a=self.getPinA()
		b=self.getPinB()
		if a==1 and b==1:
			return 0
		else:
			return 1

class NorGate(BinaryGate):
	def __init__(self,n):
		super().__init__(n)

	def performGateLogic(self):
		a=self.getPinA()
		b=self.getPinB()
		if a==1 or b==1:
			return 0
		else:
			return 1

class XorGate(BinaryGate):
	def __init__(self,n):
		super().__init__(n)

	def performGateLogic(self):
		a=self.getPinA()
		b=self.getPinB()
		if a==b:
			return 0
		else:
			return 1

class Connector:
	def __init__(self,fgate,tgate):
		self.fromgate=fgate
		self.togate=tgate

		tgate.setNextPin(self)

	def getFrom(self):
		return self.fromgate

	def getTo(self):
		return self.togate

class HalfAdder:
	def __init__(self,a,b):
		self.a=a
		self.b=b

	def getSum(self):
		g=XorGate("XOR")
		g.setPin(self.a)
		g.setPin(self.b)
		return g.getOutput()

	def getCarry(self):
		g=AndGate("AND")
		g.setPin(self.a)
		g.setPin(self.b)
		return g.getOutput()

class FullAdder:
	def __init__(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c

	def getSum(self):
		g1=XorGate("XOR")
		g2=XorGate("XOR")
		g1.setPin(self.a)
		g1.setPin(self.b)
		g2.setPin(self.c)
		c1=Connector(g1,g2)
		return g2.getOutput()

	def getCarry(self):
		g3=OrGate("OR")
		g4=AndGate("AND")
		g5=AndGate("AND")
		g6=OrGate("OR")
		g3.setPin(self.a)
		g3.setPin(self.b)
		g4.setPin(self.c)
		g5.setPin(self.a)
		g5.setPin(self.b)
		c2=Connector(g3,g4)
		c3=Connector(g4,g6)
		c4=Connector(g5,g6)
		return g6.getOutput()

def full_adder_8bit(num1=10001011,num2=10010001):
	s=[]
	c=0
	for i in range(8):		
		a_adder=FullAdder(num1%10,num2%10,c)
		si=a_adder.getSum()
		s.append(str(si))
		c=a_adder.getCarry()
		num1//=10
		num2//=10
	s.reverse()
	return ''.join(s)


g1=AndGate("G1")
g2=AndGate("G2")
g3=OrGate("G3")
g4=NotGate("G4")

g1.setPin(0)
g1.setPin(1)
g2.setPin(1)
g2.setPin(1)
c1=Connector(g1,g3)
c2=Connector(g2,g3)
c3=Connector(g3,g4)
print(g1.getOutput())
print(g2.getOutput())
print(g3.getOutput())
print(g4.getOutput())

print("INPUT\tOUTPUT")
print("A\tB\tC\tS")
input=[0,1]
for A in input:
	for B in input:
		half_adder=HalfAdder(A,B)
		S=half_adder.getSum()
		C=half_adder.getCarry()
		print(str(A)+"\t"+str(B)+"\t"+str(C)+"\t"+str(S))

print("INPUT\t\tOUTPUT")
print("C_\tA\tB\tS\tC")
input=[0,1]
for C_ in input:
	for A in input:
		for B in input:
			full_adder=FullAdder(A,B,C_)
			S=full_adder.getSum()
			C=full_adder.getCarry()
			print(str(C_)+"\t"+str(A)+"\t"+str(B)+"\t"+str(S)+"\t"+str(C))

print(full_adder_8bit())
