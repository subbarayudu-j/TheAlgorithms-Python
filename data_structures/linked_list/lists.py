mylist=list()  #Created a list

# Inserting an element
element=int(input("Enter the element:"))
mylist.append(element)
print(mylist)

#Traversing a list through index
flag=0   
selement=int(input("Enter search element:"))
for i in range(len(mylist)):
    if(mylist[i]==selement):
        print("Element Found at index:",i)
        flag=1
        break
if(flag==0):
    print("Element not found")


#Traversing a list through element
flag=0   
selement=int(input("Enter search element:"))
for i in mylist:
    if(i==selement):
        print("Element Found at index:",i)
        flag=1
        break
if(flag==0):
    print("Element not found")

#Deleting an element through index
index=int(input("Enter the index to be deleted:"))
del(mylist[index])
print(mylist)
#or
mylist.pop(index)

print(mylist)

    
