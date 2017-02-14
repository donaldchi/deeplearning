#!/usr/bin/env python3
#coding: utf-8
import numpy as np
import matplotlib.pylab as plt

A = np.array([1, 2, 3, 4])
print("Array: ", A)
print("dim: ", np.ndim(A))
print("shape: ", A.shape)
print("shape[0]: ", A.shape[0])

B = np.array([[1,2],[3,4],[5,6]])
print(B)
print(np.ndim(B))

C = np.array([[7, 8, 9],[10, 11, 12]])

print("内積: ", np.dot(B, C))
