#!/usr/bin/env python
# coding: utf-8

# In[104]:


import numpy as np


# Orthogonal diagonolisation of a matrix
a = np.array([[1, -2, 4], [-2, -1, -2], [4, -2, 5]])


def orthogonalDiag(matrix):
    eigValues, eigVectors = np.linalg.eig(matrix)
    basisVectors = orthoNormalBasis(eigVectors.T)
    q_vector = np.column_stack(basisVectors)
    d_vector = np.dot(q_vector.T, np.dot(matrix, q_vector))
    return q_vector, d_vector


def orthoNormalBasis(eVectors):
    orthNormBasis = []
    for x in eVectors:
        i = eVectors - sum(np.dot(vector, b) * b for b in orthNormBasis)
        orthNormBasis.append(i / np.linalg.norm(i))
        return orthNormBasis

q, d = orthogonalDiag(a)
np.dot(q, np.dot(d, q.T))


# QR Decomposition of a matrix
a = [[[2, -2, 4], [-2, -1, -2], [4, -2, 5]]]

q, d = orthogonalDiag(a)
r = np.dot(q.T, a)
