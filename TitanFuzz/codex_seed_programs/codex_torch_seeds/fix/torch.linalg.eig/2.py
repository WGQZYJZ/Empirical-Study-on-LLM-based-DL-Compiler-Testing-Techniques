'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eig\ntorch.linalg.eig(A, *, out=None)\n'
import torch
A = torch.randn(3, 3)
(eigen_values, eigen_vectors) = torch.linalg.eig(A)
print('Eigen values\n', eigen_values)
print('Eigen vectors\n', eigen_vectors)