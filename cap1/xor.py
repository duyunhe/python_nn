# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 17:31
# @Author  : yhdu@tongwoo.cn
# @简介    : 
# @File    : xor.py

from network import NeuralNetwork
import numpy as np


def get_training_data():
    data_list = []
    with open("./data/input.txt") as fp:
        for line in fp:
            items = map(int, line.strip('\n').split(','))
            data_list.append(items)
    return data_list


def judge(x):
    return 1 if x > .5 else 0


def main():
    i_num, h_num, o_num, learning_rate = 3, 5, 2, 0.1
    nn = NeuralNetwork(i_num, h_num, o_num, learning_rate)
    training_data = get_training_data()
    vec = np.array(training_data)
    q = vec[:, 0:i_num]
    o = vec[:, i_num:].T
    for i in range(10000):
        for record in training_data:
            input_list, target = record[0:i_num], [record[i_num:]]
            nn.train(inputs_list=input_list, targets_list=target)
        if i % 1000 == 0:
            print i, nn.calc_loss(q, o)
    print nn.query(q)


main()
