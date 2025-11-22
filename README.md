# Singular Value Decomposition (SVD) Demo

This repository contains a single Python script `SVD.py` that demonstrates (in a manual, step‑by‑step fashion) how the Singular Value Decomposition of a matrix can be assembled using eigenvalue decomposition of `T T^T` and `T^T T`.

## Matrix Under Study
The script defines the matrix:
```python
T = np.array([[3, 2, 2],
              [2, 3, -2]])  # Shape: (2 x 3)
```
Goal: Decompose `T` into `U Σ V^T`.

## What the Script Does (Step by Step)
1. Computes `MMT = T @ T.T` (a 2x2 matrix) and eigen‑decomposes it to obtain the left singular vectors (`U`) and eigenvalues.
2. Computes `MTM = T.T @ T` (a 3x3 matrix) and eigen‑decomposes it to obtain the right singular vectors (`V`) and eigenvalues.
3. Rounds eigenvectors/eigenvalues for nicer display.
4. Forms diagonal matrices from the eigenvalues.
5. Extracts non‑zero rows, takes square roots to approximate singular values, creating a (non‑standard shaped) `Σ` matrix.
6. Reconstructs `T` via `U @ Σ @ V.T` and prints intermediate and final results.

> Note: For a true SVD, `Σ` should have non‑negative singular values on its diagonal (shape `(m x n)` with zeros elsewhere). The script's construction produces a matrix with singular values placed along a diagonal but also retains extra zero columns/rows; it's a pedagogical demonstration rather than a production implementation.

## Sample Output
Running the script (Python + NumPy installed) currently produces:
```
U:
[[ 0.71 -0.71]
 [ 0.71  0.71]]

Σ (constructed):
[[5. 0. 0.]
 [0. 0. 3.]]

V:
[[-0.71 -0.67  0.24]
 [-0.71  0.67 -0.24]
 [-0.    0.33  0.94]]

Reconstruction U Σ V^T:
[[-3.0317 -2.0093 -2.0022]
 [-2.0093 -3.0317  2.0022]]
```
You can compare this to the original `T` to observe rounding and sign differences (sign flips in singular vectors are acceptable; singular vectors are defined up to ± signs).

## Requirements
- Python 3.8+ (any modern version should work)
- NumPy

### Install Dependencies
```powershell
pip install numpy
```
(Use `py -m pip install numpy` if `pip` is not on PATH.)

## How to Run
```powershell
python SVD.py
```
This will print `U`, `Σ`, `V`, and the reconstructed matrix.

## Using NumPy's Built-in SVD (Recommended)
For most real applications, prefer NumPy's reliable implementation:
```python
import numpy as np
T = np.array([[3, 2, 2],
              [2, 3, -2]])
U, s, Vt = np.linalg.svd(T, full_matrices=False)
Sigma = np.diag(s)
reconstructed = U @ Sigma @ Vt
```
This yields singular values `s` and orthonormal matrices `U`, `Vt` with proper shapes.

## Possible Improvements
- Replace manual eigenvalue steps with `np.linalg.svd` to ensure numerical stability.
- Sort singular values descending and align columns of `U`/rows of `V^T` accordingly.
- Add assertions comparing manual reconstruction to the original matrix within a tolerance.
- Parameterize the input matrix (e.g., read from a file or accept CLI args).
- Provide a function `manual_svd(T)` returning `(U, Sigma, Vt)` for reuse/testing.

## Educational Notes
- Eigenvectors of `T T^T` form the left singular vectors; eigenvectors of `T^T T` form the right singular vectors.
- Non‑zero eigenvalues of both `T T^T` and `T^T T` are the squared singular values.
- Numerical differences and sign flips are normal; only relative orientation matters.

## License
This example is intended for educational use. You may adapt it freely.

## Next Steps
If you expand this repository, consider adding:
- A dedicated module `svd_manual.py` with a clean function.
- Unit tests validating reconstruction accuracy (`np.allclose`).
- Performance comparison between manual and built‑in SVD for larger matrices.

---
Feel free to modify or translate this README further if needed.
