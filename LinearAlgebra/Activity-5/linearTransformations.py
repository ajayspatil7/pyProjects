"""
Write a Python program to input any vector and implement the following linear
transformations on them:
1. Rotation by any angle about any given point in R^3
2. Translation by user given input coordinates in R (is linear in R^3).
3. Shear by a user given value k.
For both x and y axes.
4. Non-uniform Scaling by user given input values sx and sy.
5. • Reflection about x-axis.
• Reflection about y-axis.
"""
import numpy as np
from math import radians, cos, sin


def rotate_vector(vector, theta, x0, y0):
    x, y = vector
    theta = radians(theta)
    c = cos(theta)
    s = sin(theta)
    # Translation to origin
    x -= x0
    y -= y0
    # Rotation about x-axis
    new_x = x*c - y*s
    new_y = x*s + y*c
    # Translation back to original position
    new_x += x0
    new_y += y0
    return np.array([new_x, new_y])

# Define the vertices of the square
square = np.array([[0, 0, 1], [0, 3, 1], [3, 0, 1], [3, 3, 1]])

# Define the translation matrices
T1 = np.array([[1, 0, 2], [0, 1, 2], [0, 0, 1]])
T2 = np.array([[1, 0, -1], [0, 1, -1], [0, 0, 1]])

# Define the reflection matrix about the x-axis
R_x = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])

# Define the reflection matrix about the y-axis
R_y = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])

# Define the rotation matrix about the origin by 45 degrees
theta = np.radians(45)
R = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])

# Define the scaling matrix with factors 2 and 3
S = np.array([[2, 0, 0], [0, 3, 0], [0, 0, 1]])

# Define the shear matrix with factors 1 and 2
Sh = np.array([[1, 2, 0], [0, 1, 0], [0, 0, 1]])

# Perform the translations and transformations
print("Original square: ", square)
print("Translated square: ", np.dot(T1, square.T).T)
print("Translated and reflected about x-axis square: ", np.dot(R_x, np.dot(T2, square.T)).T)
print("Rotated square: ", np.dot(R, square.T).T)
print("Scaled square: ", np.dot(S, square.T).T)
print("Sheared square: ", np.dot(Sh, square.T).T)
print("Reflected about y-axis square: ", np.dot(R_y, square.T).T)

# Test the rotate_vector function
print(rotate_vector([0, 0], 45, 0, 0))
