a=[1,0,2,50,6,20,0,2]
i,count=0,0
b=[]
while i<len(a) :
    if a[i]!=0 :
        b.append(a[i])
        count+=1
    i+=1
for i in range(count,len(a)) :
    b.append(0)
print(b)

