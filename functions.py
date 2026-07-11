def fact(m) :
    if m==0 :
        return 1
    return fact(m-1)*m

def sum(n) :
    if n==0:
        return 0
    return n+sum(n-1)


def fibo(n) :
    if n==0 :
        return
    elif n==1 :
        return
    return fibo(n-1)+fibo(n-2)