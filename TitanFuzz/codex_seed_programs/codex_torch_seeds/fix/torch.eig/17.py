'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
input = torch.randn(3, 3)
(eigen_values, eigen_vectors) = torch.eig(input, True)
print('Input: \n', input)
print('Eigenvalues: \n', eigen_values)
print('Eigenvectors: \n', eigen_vectors)