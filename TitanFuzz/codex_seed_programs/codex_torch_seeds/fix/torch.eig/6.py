'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
input = torch.randn(3, 3, dtype=torch.float64, requires_grad=True)
print('input = ', input)
(eigen_values, eigen_vectors) = torch.eig(input, eigenvectors=True)
print('eigen_values = ', eigen_values)
print('eigen_vectors = ', eigen_vectors)
eigen_values = torch.eig(input, eigenvectors=False)
print('eigen_values = ', eigen_values)