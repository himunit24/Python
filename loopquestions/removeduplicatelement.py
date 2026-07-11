elements = input("Enter your elements separated by space : ")
l1=[int(x) for x in elements if x.isdigit()]
for i in range(len(l1)) :
    j=i+1
    while j<len(l1) :
        if l1[i]==l1[j] :
            l1.remove(l1[j])
        else : 
            j=j+1
print(l1)