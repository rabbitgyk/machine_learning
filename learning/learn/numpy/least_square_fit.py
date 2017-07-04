# -*- coding: utf-8 -*-
import numpy as np
import scipy.optimize as opt
import matplotlib.pylab as pl


def func(x, p):
    """
    数据拟合所用的函数: A*sin(2*pi*k*x + theta)
    """
    (A, k, theta)  = p
    return A*np.sin(2*np.pi*k*x+theta)

def residuals(p, y, x):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x, p)

x0 = np.linspace(0, -2*np.pi, 100)
A0, k0, theta0 = 10, 0.34, np.pi/6 # 真实数据的函数参数
y0 = func(x0, [A0, k0, theta0]) # 真实数据
y1 = y0 + 2 * np.random.randn(len(x0)) # 加入噪声之后的实验数据

p0 = [7, 0.2, 0] # 第一次猜测的函数拟合参数

# 调用leastsq进行数据拟合
# residuals为计算误差的函数
# p0为拟合参数的初始值
# args为需要拟合的实验数据
result_vector = opt.leastsq(residuals, p0, args=(y1, x0))

print("real params:", [A0, k0, theta0])
print("fit params:", result_vector[0]) # 实验数据拟合后的参数

pl.plot(x0, y0, label="real data")
pl.plot(x0, y1, label="test data")
pl.plot(x0, func(x0, result_vector[0]), label="fit data")
pl.legend()
pl.show()