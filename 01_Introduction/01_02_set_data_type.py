#set data type
#list
myList=[1,3,True,6.5]
print(myList)
myList=[0]*6
print(myList)
myList=[1,2,3,4]
A=[myList]*3
print(A)
myList[2]=45
print(A)

myList=[1024,3,True,6.5]
print(myList)
myList.append(False)
print(myList)
myList.insert(2,4.5)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
print(myList.pop(2))
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)

add=(54).__add__(21)
print(add)

print(range(10))
print(list(range(10)))
print(list(range(5,10)))
print(list(range(10)))
print(list(range(5,10,2)))
print(list(range(10,1,-1)))

#string
myName="David"
print(myName)
print(myName[3])
print(myName*2)
print(len(myName))
print(myName.upper())
print(myName.center(10))
print(myName.find('v'))
print(myName.split('v'))

#tuple
myTuple=(2,True,4.96)
print(myTuple)
print(len(myTuple))
print(myTuple[0])
print(myTuple*3)
print(myTuple[0:2])

#set
mySet={3,6,"cat",4.5,False}
print(mySet)
print(len(mySet))
print(False in mySet)
print("dog" in mySet)

yourSet={99,3,100}
print(mySet.union(yourSet))
print(mySet|yourSet)
print(mySet.intersection(yourSet))
print(mySet&yourSet)
print(mySet.difference(yourSet))
print(mySet-yourSet)
print({3,100}.issubset(yourSet))
print({3,100}<=yourSet)
mySet.add("house")
print(mySet)
mySet.remove(4.5)
print(mySet)
print(mySet.pop())
print(mySet)
mySet.clear()
print(mySet)

#dictionary
capitals={'Iowa':'DesMonines','Wiasconsin':'Madison'}
print(capitals)
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(capitals)
print(len(capitals))

phoneext={'david':1410,'brad':1137}
print(phoneext)
print(phoneext.keys())
print(phoneext.values())
print(phoneext.items())
print(list(phoneext.items()))
print(phoneext.get('kent'))
print(phoneext.get('kent','NO ENTRY'))
