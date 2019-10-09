#Creation of a tuple
Tuple=tuple()

#Insertion of an element
Tuple=Tuple+(1,)

#Accessing an element
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

#This will give the result as:
#tup1[0]:  physics
#tup2[1:5]:  (2, 3, 4, 5)

#Creating a new Tuple by existing tuples
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)

#This will be the result
#(12, 34.56, 'abc', 'xyz')

#Deletion of a tuple
del tup;
print ("After deleting tup : ")
print (tup)
# It will give an error as tuple is deleted
