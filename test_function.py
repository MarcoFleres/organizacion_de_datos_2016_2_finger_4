def myhash(s):
	a = 0
	for i, c in enumerate(s):
		if c.isalpha() :
			a += 4000000/(54*2**(i-1))*(ord(c)-40)
		else:
			a += ord(c)


	if(len(s) % 3 == 0):
		a *= 3

	return a

i=0
col=0
noncol = 0
d=dict()
with open('words.txt') as f:
	for line in f:
		i=i+1
		z = myhash(line) % 400000
		if z in d:
			col = col + 1
			d[z]+=1
		else:
			noncol = noncol+1
			d[z]=1
print "Number of lines in file: "+str(i)
print "Collisions: " +str(col)
print "Non Collisions: "+str(noncol)
print "Total keys: "+str(col+noncol)

