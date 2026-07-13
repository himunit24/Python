def add(a,b) :
    return a+b

x=add
y=x
print(y(5,5))
print(x(6,5))
print(id(add),id(x),id(y))


a=lambda a : print(a)
a(10)

(lambda a : print(a*10))(10)

f=lambda a : 1 if a==0 or a==1 else a*f(a-1)
print(f(999))