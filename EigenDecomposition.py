"""Eigen decomposition demo

This small script constructs a 3x3 matrix, computes its eigenvalues and
eigenvectors using NumPy, and demonstrates reconstruction of the original
matrix from its eigendecomposition.

Changes made:
- Added English comments and a short module docstring.
- Renamed variables to be more descriptive: T -> A, a -> A_reconstructed.
"""

import math
import numpy as np

# Define a 3x3 example matrix (call it A to be conventional)
A = np.array([
    [4, -2, 5],
    [1,  1, 6],
    [6,  4, 7],
])

# Print the original matrix
print("Original matrix A:")
print(A)

# Compute eigenvalues and (right) eigenvectors of A
# eigenvalues: 1D array of eigenvalues
# eigenvectors: columns are the eigenvectors corresponding to eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(A)

# Round for easier reading when printing (not for computation accuracy)
eigenvalues = np.round(eigenvalues, 2)
eigenvectors = np.round(eigenvectors, 2)

print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors (columns):")
print(eigenvectors)

# Reconstruct the original matrix from eigenvectors * diag(eigenvalues) * inv(eigenvectors)
# This demonstrates that A = V * D * V^{-1} for a diagonalizable matrix
A_reconstructed = eigenvectors @ np.diag(eigenvalues) @ np.linalg.inv(eigenvectors)
A_reconstructed = np.round(A_reconstructed, 2)

print("\nReconstructed A from eigen-decomposition:")
print(A_reconstructed)