#more ways to create array
import numpy as n
a=n.zeros((3,1),dtype='i4')
print(a)
print()
b=n.ones((4,7),dtype='i8')
print(b)
print()
c=n.full((3,3),22,dtype='i4')
print(c)
print()
d=n.arange(8)  #like range function
print(d)
print(d.reshape(2,2,2))
print()
y=n.linspace(1,10,20) # 20 mtlb element rakhenge aur gap apne aap decide hoga 1 se 10 ke beech jbki hm range me gap bhi khud hi 
print(y)             #decide krte hai
z=n.array([[1,2,3],[4,5,6],[7,8,9]],dtype='f4') #nan values can only be applied to float arryas as nan is of float
z[1,1]=n.nan
print(z)
print()
h=n.identity(3,dtype='i4')
print(h)

