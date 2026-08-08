n=int(input("Enter number"))
i=2
a=0
while i<n :
    if(n%i==0) :
        a=1
        break
    i=i+1
if(a==1) :
    print("Composite")
else :
    print("Prime")