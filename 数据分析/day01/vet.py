"""
# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 9:32
# @Author  : franck
# @Email   : franck_gxu@outlook.com
"""

from __future__ import unicode_literals
import datetime as dt
import numpy as np
start = dt.datetime.now()
n = 100000
a,b = [],[]
for i in range(n):
    a.append(i**2)
    b.append(i**3)
c = []
for a,b in zip(a,b):
    c.append(a+b)
end = dt.datetime.now()
print((end-start).microseconds)

start1 = dt.datetime.now()
A,B = np.arange(n) ** 2,np.arange(n) ** 3 #返回一个数组
C=A+B
end1 = dt.datetime.now()
print((end1-start1).microseconds)

