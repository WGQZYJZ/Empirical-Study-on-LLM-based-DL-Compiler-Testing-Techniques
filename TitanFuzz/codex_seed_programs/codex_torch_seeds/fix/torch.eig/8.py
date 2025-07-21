'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(3, 3)
print('Input data: \n', input)
print('Task 3: Call the API torch.eig')
(eigen_values, eigen_vectors) = torch.eig(input, eigenvectors=True)
print('Eigen values: \n', eigen_values)
print('Eigen vectors: \n', eigen_vectors)