#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
my_list = [1, 2, 3, 4, 5]
a = 10
my_matrix = np.mat(my_list)

print(a * my_matrix)

my_zero = np.zeros([3,5])
print(my_zero)

my_one = np.ones([3,3])
print(my_one)

my_random = np.random.rand(3,4)
print(my_random)

my_eye = np.eye(3)
print(my_eye)

print(my_one-my_eye)

y_matrix = np.mat([[1,2,3],[4,5,6],[7,8,9]])
print(a*y_matrix)

print(np.sum(y_matrix))

print(y_matrix.T)

print(y_matrix.transpose())
[m,n]=np.shape(y_matrix)
print(m)
print(y_matrix[0])
#方阵的行列式
print(np.linalg.det(my_eye))
#矩阵的逆
print(np.linalg.inv(y_matrix))

print(y_matrix+y_matrix.T)
#矩阵的秩
print(np.linalg.matrix_rank(y_matrix))

