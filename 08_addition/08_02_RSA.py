import random
def encrypt(m):
	s='abcdefghigklmnopqrstuvwxyz'
	n=''
	for i in m:
		j=(s.find(i)+13)%26
		n=n+s[j]
	return n

def decrypt(m,k):
	s='abcdefghigklmnopqrstuvwxyz'
	n=''
	for i in m:
		j=(s.find(i)+26-k)%26
		n=n+s[j]
	return n

def modexp(x,n,p):
	if n==0:
		return 1
	t=(x*x)%p
	tmp=modexp(t,n//2,p)
	if n%2!=0:
		tmp=(tmp*x)%p
	return tmp

def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

def ext_gcd(x,y):
	if y==0:
		return(x,1,0)
	else:
		(d,a,b)=ext_gcd(y,x%y)
		return(d,b,a-(x//y)*b)

def RSAgenkeys(p,q):
	n=p*q
	pqminus=(p-1)*(q-1)
	e=int(random.random()*n)
	while gcd(pqminus,e)!=1:
		e=int(random.random()*n)
	d,a,b=ext_gcd(pqminus,e)
	if b<0:
		d=pqminus+b
	else:
		d=b
	return((e,d,n))

def RSAencrypt(m,e,n):
	chunks=toChunks(m,n.bit_length()//8*2)
	encList=[]
	for messchunk in chunks:
		c=modexp(messchunk,e,n)
		encList.append(c)
	return encList

def RSAdecrypt(chunkList,d,n):
	rList=[]
	for c in chunkList:
		m=modexp(c,d,n)
		rList.append(m)
	return chunksToPlain(rList,n.bit_length()//8*2)

def toChunks(m,chunkSize):
	byteMess=bytes(m,'utf-8')
	hexString=''
	for b in byteMess:
		hexString=hexString+("%02x"%b)

	numChunks=len(hexString)//chunkSize
	chunkList=[]
	for i in range(0,numChunks*chunkSize+1,chunkSize):
		chunkList.append(hexString[i:i+chunkSize])
	chunkList=[eval('0x'+x) for x in chunkList if x]
	return chunkList

def chunksToPlain(clist,chunkSize):
	hexList=[]
	for c in clist:
		hexString=hex(c)[2:]
		clen=len(hexString)
		hexList.append('0'*((chunkSize-clen)%2)+hexString)

	hstring=''.join(hexList)
	messArray=bytearray.fromhex(hstring)
	return messArray.decode('utf-8')

e,d,n=RSAgenkeys(5563,8191)
c=RSAencrypt('goodbye girl',e,n)
m=RSAdecrypt(c,d,n)
print(m)









