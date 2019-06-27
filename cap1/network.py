# -*- coding: utf-8 -*-
# @Time    : 2019/6/27 8:59
# @Author  : yhdu@tongwoo.cn
# @简介    : 
# @File    : network.py


import numpy as np
import scipy.special


class NeuralNetwork:

    def __init__(self, input_nodes=2, hidden_nodes=2, output_nodes=1, learning_rate=.1):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.lr = learning_rate

        # self.wih = np.random.rand(hidden_nodes, input_nodes) - 0.5
        # self.who = np.random.rand(output_nodes, hidden_nodes) - 0.5

        self.wih = np.random.normal(0.0, self.hidden_nodes ** -.5, (self.hidden_nodes, self.input_nodes))
        self.who = np.random.normal(0.0, self.output_nodes ** -.5, (self.output_nodes, self.hidden_nodes))

        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    def train(self, inputs_list, targets_list):
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T
        hidden_outputs = self.activation_function(np.dot(self.wih, inputs))
        outputs = self.activation_function(np.dot(self.who, hidden_outputs))

        output_errors = targets - outputs
        hidden_errors = np.dot(self.who.T, output_errors)

        self.who += self.lr * np.dot((output_errors * outputs * (1 - outputs)), hidden_outputs.T)
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1 - hidden_outputs)), inputs.T)
        pass

    def query(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        hidden_outputs = self.activation_function(np.dot(self.wih, inputs))
        outputs = self.activation_function(np.dot(self.who, hidden_outputs))
        return outputs

    def calc_loss(self, inputs_list, targets):
        predict = self.query(inputs_list)
        loss = 0.5 * np.sum((predict - targets) ** 2)
        return loss
