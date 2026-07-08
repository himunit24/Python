x=str(input())
y,z=0,0
for i in x :
    if i.isupper() :
        y+=1
    elif i.islower() :
        z+=1
print("Uppercase",y)
print("Lowercase",z)