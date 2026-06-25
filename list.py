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