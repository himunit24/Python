l1=[40,20,30,10,50]
print(l1[2])
print(l1[1],l1[-4],l1[-1]) #same hai isme negative indexing ka concept hota hai aur last se shuru hota hai -1 se shuru hota hai
print("____________________________________________________________________________________________")
l2=[10,50,30,40,20]
for i in l2 :
    print(i,end=" ")
print()
print("-----------------------------------------------------")
# we can also use while loop here
i=len(l2)-1
while i>=0 :
    print(l2[i],end=" ")
    i=i-1

#for deleting element use del(l2[0])
del(l2[2])
print()
print("-----------------------------------------------------")
# we can also use while loop here
i=len(l2)-1
while i>=0 :
    print(l2[i],end=" ")
    i=i-1

print()
l5=list(range(4))
l6=list(range(5))
print(l5)
print(l6>l5)
print(l6+l5)
l7=l6*2
print(l7)

l1.append(10)
l1.insert(2,100)
print(l1)
l1.remove(10) # if two values are present then 1 occuring value will be deleted
print(l1)
x=l1.pop() #it deleted last element and gives its value therefore it is stored
print(x)
print(l1)
l7.clear() #it removes all element ina list
print(l7)
l1.reverse()
print(l1)
print(l1.index(50))

#list comprehension
n=int(input("Enter a number : "))
l10=[a*2-1 for a in range(1,n+1)] 
l9=[a*2 for a in range(1,int(input("Enter nth term : "))+1)]
print(l10,l9)