#!/usr/bin/env python
#coding: utf-8
#usage: simple neural network without activation function

import numpy as np

A = np.array([1, 2])
W = np.array([[1, 3, 5], [2, 4, 6]])

Y = np.dot(A, W)
print(Y)
