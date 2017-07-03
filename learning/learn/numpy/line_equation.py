#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

# 解方程组
A = np.mat([[1,2,4,5,7,],[9,12,11,8,2,],[6,4,3,2,1,],[9,1,3,4,5],[0,2,3,4,1]])
b = [1, 0, 1, 0, 1]
S = np.linalg.solve(A, b)
print(S)

# 向量范数
aa = [8, 1, 6]
modAA = np.sqrt(np.sum(np.power(aa, 2)))
print(modAA)

normAA = np.linalg.norm(aa)
print(normAA)
