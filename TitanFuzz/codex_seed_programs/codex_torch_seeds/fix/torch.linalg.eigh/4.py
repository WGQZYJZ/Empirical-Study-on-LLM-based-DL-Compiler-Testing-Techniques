"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eigh\ntorch.linalg.eigh(A, UPLO='L', *, out=None)\n"
import torch
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A = torch.from_numpy(A).float()
print('Input data is:')
print(A)
print('Task 3: Call the API torch.linalg.eigh')
(eigen_values, eigen_vectors) = torch.linalg.eigh(A)
print('Eigen values are:')
print(eigen_values)
print('Eigen vectors are:')
print(eigen_vectors)