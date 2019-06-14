# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 14:01
# @Author  : yhdu@tongwoo.cn
# @简介    : 
# @File    : simple_neutron.py

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1.0 / (1 + np.e ** -x)


def draw():
    x = np.linspace(-10, 10, 1000)
    y = sigmoid(x)
    plt.figure(num=1, figsize=(10, 6))
    plt.plot(x, y)  # 画默认线
    plt.title('Matplotlib Test')
    plt.show()


def calc():
    mat1 = np.array([[0.9, 0.3, 0.4], [0.2, 0.8, 0.2], [0.1, 0.5, 0.6]])
    mat2 = np.array([[0.3, 0.7, 0.5], [0.6, 0.5, 0.2], [0.8, 0.1, 0.9]])
    w = np.array([[0.9, 0.1, 0.8]]).transpose()
    print w.ndim
    o1 = sigmoid(np.dot(mat1, w))
    print o1
    out = sigmoid(np.dot(mat2, o1))

    print out
    print np.dot(w.transpose(), w)


def draw_node():
    fig = plt.figure(num=1, figsize=(10, 6))
    text_params = {'ha': 'center', 'va': 'center', 'family': 'SimHei', 'fontweight': 'bold'}
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    text_size = 35
    arrow_alpha = 0.5

    plt.arrow(1.5, 7.4, 2.7, 0, shape='right', head_width=0.5, width=0.2,
              head_length=0.3, fill=True, alpha=arrow_alpha, color='red')
    plt.arrow(1.6, 7, 2.6, -3.8, shape='right', head_width=0.5, width=0.2, head_length=0.3, fill=True, alpha=arrow_alpha,
              color='red')
    plt.arrow(1.5, 2.6, 2.7, 0, shape='right', head_width=0.5, width=0.2, head_length=0.3, fill=True, alpha=arrow_alpha,
              color='red')
    plt.arrow(1.6, 3, 2.6, 3.8, shape='right', head_width=0.5, width=0.2, head_length=0.3, fill=True, alpha=arrow_alpha,
              color='red')

    plt.arrow(5.5, 7.4, 2.7, 0, shape='right', head_width=0.5, width=0.2, head_length=0.3, fill=True, alpha=arrow_alpha,
              color='b')
    plt.arrow(5.6, 7, 2.6, -3.8, shape='right', head_width=0.5, width=0.2, head_length=0.3, fill=True,
              alpha=arrow_alpha, color='b')
    plt.arrow(5.5, 2.6, 2.7, 0, shape='right', head_width=0.5, width=0.2, head_length=0.3, fill=True, alpha=arrow_alpha,
              color='b')
    plt.arrow(5.6, 3, 2.6, 3.8, shape='right', head_width=0.5, width=0.2, head_length=0.3, fill=True, alpha=arrow_alpha,
              color='b')

    i0 = plt.text(1, 7, '$I_0$', color='k', size=text_size, **text_params)
    i1 = plt.text(1, 3, '$I_1$', color='k', size=text_size, **text_params)
    h0 = plt.text(5, 7, '$H_0$', color='k', size=text_size, **text_params)
    i1 = plt.text(5, 3, '$H_1$', color='k', size=text_size, **text_params)
    o0 = plt.text(9, 7, '$O_0$', color='k', size=text_size, **text_params)
    o1 = plt.text(9, 3, '$O_1$', color='k', size=text_size, **text_params)

    plt.show()
