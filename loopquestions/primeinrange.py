a=int(input())
b=int(input())
for i in range(a,b+1) :
    x=0
    for j in range(2,i) :
        if i%j==0 :
            x=1
            break
    if x==0 :
        print(i,end=" ")