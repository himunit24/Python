n=int(input("Enter your number : "))
z=0
for i in range(1,n) :
    if(n%i==0) :
        z=1
        break
    i=i+1
if z==0 :
    print("prime")
else :
    print("composite")