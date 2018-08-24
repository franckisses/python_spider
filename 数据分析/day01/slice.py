# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
# a = np.arange(1, 10)
# print(a)  # 1 2 3 4 5 6 7 8 9
# print(a[:3])  # 1 2 3
# print(a[3:6])  # 4 5 6
# print(a[6:])  # 7 8 9
# print(a[::-1])  # 9 8 7 6 5 4 3 2 1
# print(a[:-4:-1])   # 9 8 7
# print(a[-4:-7:-1])  # 6 5 4
# print(a[-7::-1])  # 3 2 1
# print(a[::])
# print(a[:])
# print(a[...])
# print(a[::3])  # 1 4 7
# print(a[1::3])  # 2 5 8
# print(a[2::3])  # 3 6 9
b = np.arange(1, 25).reshape(2, 3, 4)
# print(b)
# [[[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# [[13 14 15 16]
#  [17 18 19 20]
#  [21 22 23 24]]]
# print(b[:, 0, 0])  #[ 1 13]
# print(b[0, :, :])
# [[ 1  2  3  4]
# [ 5  6  7  8]
# [ 9 10 11 12]]
# print(b[0, ...])
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
# print(b[0, 1, ::2])
# [5 7]
# print(b[..., 1])
# [[ 2  6 10]
# [14 18 22]]
print(b[::-1, ::-1])

# print(b[-1, 1:, 2:])
# [[19 20]
# [23 24]]
