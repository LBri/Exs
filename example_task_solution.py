import sys
# missing input files
# input = (0,-10,8,12,-1)
n=int(input())
if n == 0:
	print (0)
	sys.exit()
	
t = input()

m = map(int(t.split(' ')))
q = m[0]

for i in range(t):
	a = abs(m[i])
	b = abs(q)
	
	if a<b:
		q = m[i]
	elif a == b and m[i]>q:
		q = m[i]
		
print (q)