import numpy as np
import math
T = np.array([[3,2,2],[2,3,-2]])

MMT= T @ np.transpose(T)
Y , U = np.linalg.eig(MMT)
U , Y = np.round(U,2),np.round(Y,2)
Y = np.diag(Y)

MTM = np.transpose(T) @ T
Y2 , V = np.linalg.eig(MTM)
V , Y2 = np.round(V,2),np.round(Y2,2)
Y2 = np.diag(Y2)

Y2 = Y2[~np.all(Y2 == 0, axis=1)]
Y2 = np.sqrt(Y2)

print(U)
print(Y2)
print(V)


print(U@Y2@V.T)