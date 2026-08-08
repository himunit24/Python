def pro(x) :
    print(x.shape)
    print(x.ndim)
    print(x.size)
    print(type(x))

import numpy as n

a1=n.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
a2=n.array([[[[[1,2,3]]]],[[[[4,5,6]]]],[[[[7,88,9]]]]])
pro(a1)
print()
print()
pro(a2)