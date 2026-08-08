import numpy as np
a=np.array([10,20,30,40,50])
two_darray=np.array([[10,20,30],[40,50,60]]) #we have to make one list
print(a)
print(*a)
print(two_darray)
print()
print()
c=np.array([[ [1,3],[2,5],[7,9] ],[ [4,8],[5,1],[6,9] ]])
print(c)
print()

d=np.array([1,2,3,4,5],dtype='i4') #i for integer and 4 means 4bytes