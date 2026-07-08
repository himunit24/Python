n=int(input())
x=str(n)
even,odd=0,0
for i in x :
#we have to convert x into integer using int
    if int(i)%2==0 :  
        even+=1
    else :
        odd+=1
print("Even Count : ",even)
print("Odd count : ",odd)