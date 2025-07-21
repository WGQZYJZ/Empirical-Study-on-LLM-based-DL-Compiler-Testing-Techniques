'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.eig\ntorch.linalg.eig(A, *, out=None)\n'
import torch
A = torch.randn(3, 3)
(eigen_values, eigen_vectors) = torch.linalg.eig(A)
print(f'Eigen values: {eigen_values}')
print(f'Eigen vectors: {eigen_vectors}')