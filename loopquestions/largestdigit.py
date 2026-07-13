n=int(input())
a=0
while n!=0 :
    b=n%10
    if b>=a :
        a=b
    n=n//10
print(a)