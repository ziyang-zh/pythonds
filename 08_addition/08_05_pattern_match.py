def simpleMatcher(pattern,text):
	starti=0
	i=0
	j=0
	match=False
	stop=False
	while not match and not stop:
		if text[i]==pattern[j]:
			i=i+1
			j=j+1
		else:
			starti=starti+1
			i=starti
			j=0

		if j==len(pattern):
			match=True
		else:
			if i==len(text):
				stop=True

	if match:
		return i-j
	else:
		return -1

def mismatchLinks(pattern):
	augPattern="0"+pattern
	links={}
	links[1]=0
	for k in range(2,len(augPattern)):
		s=links[k-1]
		stop=False
		while s>=1 and not stop:
			if augPattern[s]==augPattern[k-1]:
				stop=True
			else:
				s=links[s]
		links[k]=s+1
	return links

text='ACGACACATAGTCACTTGGCA'
pattern='ACATA'
print(simpleMatcher(pattern,text))
print(mismatchLinks(pattern))