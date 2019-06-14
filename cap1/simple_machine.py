# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 18:27
# @Author  : yhdu@tongwoo.cn
# @简介    : 
# @File    : simple_machine.py


import matplotlib.pyplot as plt
import numpy as np


def draw(x, y):
    plt.figure(num=1, figsize=(10, 6))  # 定义一个图像窗口，编号为1，大小(10,6)
    plt.plot(x, y)  # 画默认线
    # plt.plot(x, y2, color='red', linewidth=5.0, linestyle='-.')  # 设置颜色，线宽，线的样式
    plt.plot(3, 1, 'o', color='green', markersize=10)  # 画点，设置点的样式，颜色，大小
    plt.plot(1, 3, 's', color='r', markersize=10)
    # plt.axvline(0.234)
    plt.xlim(0, 4)
    plt.ylim(0, 4)
    plt.title('Matplotlib Test')
    plt.show()


def main():
    x = np.linspace(-1, 4, 20)
    y1 = 0.25 * x
    y2 = x ** 2
    y3 = np.zeros(20) + 0.5
    draw(x, y1)


def step():
    x = [3, 1]
    t = [1.1, 2.9]
    a = 0.25
    y = a * x[0]
    L = 0.5
    da = L * (t[0] - y) / x[0]
    a += da
    x1 = np.linspace(-1, 4, 20)
    y1 = a * x1
    draw(x1, y1)
    print a

    y = a * x[1]
    da = L * (t[1] - y) / x[1]
    a += da
    x2 = np.linspace(0, 4, 10)
    y2 = a * x2
    draw(x2, y2)
    print a


main()
step()
