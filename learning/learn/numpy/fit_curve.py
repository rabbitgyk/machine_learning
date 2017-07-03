#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 在指定区间返回等间隔的数字
x = np.linspace(-5, 5, 200)
# 对每一个xi计算sin函数值
y = np.sin(x)
# 对每一个y值加上一个随机向量（1行，len(y)列）
yn = y + np.random.rand(1, len(y)) * 1.5

# 创建一个图形
fig = plt.figure()
# 生成画布，并将画布分为1行2列，图形画在第一个方块内
ax = fig.add_subplot(121)
# 散点图
ax.scatter(x,yn,c='blue',marker='o')
# 曲线
ax.plot(x,y+0.75,'r')
# 展示图形
plt.show()

