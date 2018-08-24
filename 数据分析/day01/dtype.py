# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
a = np.array([20, 22, 28, 25, 19])
print(a, a.dtype)
b = np.array([20, 22, 28, 25, 19], dtype=np.uint8)
print(b, b.dtype)
c = np.array([20, 22, 28, 25, 19], dtype='uint8')
print(c, c.dtype)
d = np.array([20, 22, 28, 25, 19], dtype='u1')
print(d, d.dtype)
# 用逗号分隔每个字段的类型
e = np.array([('ABC', (1, 2, 3))], dtype='U3, 3u1')
print(e, e.dtype)
print(e[0]['f0'], e[0]['f1'])
# [(字段名, 类型, 维度), (...), ...]
f = np.array([('ABC', (1, 2, 3))], dtype=[
    ('fa', np.str_, 3), ('fb', np.uint8, 3)])
print(f, f.dtype)
print(f[0]['fa'], f[0]['fb'])
# {'names': [字段名, ...], formats: [类型, ...]}
g = np.array([('ABC', (1, 2, 3))], dtype={
    'names': ['fa', 'fb'], 'formats': ['U3', '3u1']})
print(g, g.dtype)
print(g[0]['fa'], g[0]['fb'])
# {字段名: (类型, 偏移), ...}
h = np.array([('ABC', (1, 2, 3))], dtype={
    'fa': ('U3', 0), 'fb': ('3u1', 12)})
print(h, h.dtype)
print(h[0]['fa'], h[0]['fb'])
# (原始类型, 解释类型)
i = np.array([0x1234], dtype=(
    '>u2', {'lo': ('u1', 0), 'hi': ('u1', 1)}))
print('{:x} {:x} {:x}'.format(
    i[0], i['lo'][0], i['hi'][0]))
