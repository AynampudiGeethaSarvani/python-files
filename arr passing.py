# passing array in function
import numpy as np
a=np.ndarray(shape=5,dtype=int)
def f1(a):
    print('Array values are')
    for i in range(5):
        print(a[i])
print('input array values')
for i in range(5):
    a[i]=int(input())
f1(a)
