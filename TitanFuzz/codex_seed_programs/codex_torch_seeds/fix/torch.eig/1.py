'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
input = torch.randn(2, 2)
print(input)
(eigen_values, eigen_vectors) = torch.eig(input, True)
print(eigen_values)
print(eigen_vectors)
eigen_values = torch.eig(input, False)
print(eigen_values)