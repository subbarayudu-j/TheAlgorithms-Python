def prime(x):
	l=[]
	for i in range(1,n+1):
		if x%i==0:
			l.append(i)
	return(l)
n=int(input("enter a no."))
x=prime(n)
if len(x)==2:
      print("its a prime no.")
else:
      print("not a prime")
