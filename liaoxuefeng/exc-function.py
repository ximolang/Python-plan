#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

# 空函数
def nop():
    pass

# 返回多个值
def returnVals():
    return 1,2,3

# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s

results = returnVals()
print(results[0])

print(power(10, 3))
print(power(10))

print('打印出文件列表：')
print([d for d in os.listdir('.')])
