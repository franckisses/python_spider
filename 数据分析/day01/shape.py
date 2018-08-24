# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.arange(1, 3)
print(a, a.shape, sep='\n')
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(b, b.shape, sep='\n')
c = np.array([[np.arange(1, 5),
               np.arange(5, 9),
               np.arange(9, 13)],
              [np.arange(13, 17),
               np.arange(17, 21),
               np.arange(21, 25)]])
print(c, c.shape, type(c), sep='\n')
print(a.dtype)
d = np.array(['A', 'B', 'C', 'DEF'])
print(d.dtype)
print(d)
e = d.reshape(2, 2)
print(d)
print(e)
f = a.astype(str)
print(a.dtype)
print(f.dtype)
print(f)
for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[2]):
            print(c[i][j][k], c[i, j, k])
print(c[0])
print(c[0, 0])
print(c[0, 0, 0])
