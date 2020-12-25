#input and output
#aName=input('Please enter your name: ')
aName="David"
print("Your name in all capitals is",aName.upper(),"and has length",len(aName))

#sradius=input("Please enter the radius of the circle ")
radius=2
radius=float(radius)
diameter=2*radius
print(diameter)

#format string
print("Hello")
print("Hello","world")
print("Hello","world",sep="***")
print("Hello","world",end="***\n")

age=18
print(aName,"is",age,"years old.")
print("%s is %d years old."%(aName,age))

price=24
item="banana"
print("The %s costs %d cents"%(item,price))
print("The %+10s costs %5.2f cents"%(item,price))
print("The %+10s costs %10.2f cents"%(item,price))
itemdict={"item":"banana","cost":24}
print("The %(item)s costs %(cost)7.1f cents"%itemdict)