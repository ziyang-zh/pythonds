def recMC(coinValueList,change):
	minCoins=change
	if change in coinValueList:
		return 1
	else:
		for i in [c for c in coinValueList if c<change]:
			numCoins=1+recMC(coinValueList,change-i)
			if numCoins<minCoins:
				minCoins=numCoins
	return minCoins
#print(recMC([1,5,10,25],63))

def recDC(coinValueList,change,knownResults):
	minCoins=change
	if change in coinValueList:
		knownResults[change]=1
		return 1
	elif knownResults[change]>0:
		return knownResults[change]
	else:
		for i in [c for c in coinValueList if c<change]:
			numCoins=1+recDC(coinValueList,change-i,knownResults)
			if numCoins<minCoins:
				minCoins=numCoins
				knownResults[change]=minCoins
	return minCoins
#print(recDC([1,5,10,25],63))

def dpMakeChange(coinValueList,change,minCoins,coinUsed):
	for cents in range(change+1):
		coinCount=cents
		newCoin=1
		for j in [c for c in coinValueList if c <=cents]:
			if minCoins[cents-j]+1<coinCount:
				coinCount=minCoins[cents-j]+1
				newCoin=j
			minCoins[cents]=coinCount
		coinUsed[cents]=newCoin
	return minCoins[change]

def printCoins(coinUsed,change):
	coin=change
	while coin>0:
		thisCoin=coinUsed[coin]
		print(thisCoin)
		coin=coin-thisCoin

c1=[1,5,10,21,25]
coinUsed=[0]*64
coinCount=[0]*64
print(dpMakeChange(c1,63,coinCount,coinUsed))
print(coinUsed)
print(coinCount)
printCoins(coinUsed,63)








