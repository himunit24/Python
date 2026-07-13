# write your code here
def fact(n) :
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


n=int(input())
a=n
sum=0
while n!=0 :
    sum=sum+fact(n%10)
    n=n//10
if sum==a :
    print("Strong Number")
else :
    print("Not Strong Number")