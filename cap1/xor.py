# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 17:31
# @Author  : yhdu@tongwoo.cn
# @简介    : 
# @File    : xor.py


import numpy as np


def sigmoid(x):
    return 1.0 / (1 + np.e ** -x)


def calc_error(X, T):
    i = X
    W0 = np.array([[0.6, 0.3], [0.4, 0.7]])
    # print np.dot(W0, i)
    h = sigmoid(np.dot(W0, i))
    print h
    W1 = np.array([[0.7, 0.3]])
    o = sigmoid(np.dot(W1, h))
    print o
    e = (T - o) * (1 - o) * o
    print 'e', e
    learning_rate = 0.1
    he = np.dot(e, W1)
    print he
    de = learning_rate * e
    dh = de * W1
    print dh
    W1 += dh
    # print sigmoid(np.dot(W1, h))


def main():
    X = np.array([[1, 0]]).transpose()
    T = np.array([[1]])
    calc_error(X, T)


main()
