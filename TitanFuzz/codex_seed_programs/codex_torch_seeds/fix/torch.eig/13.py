'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
input_data = torch.randn(2, 2)
print('input_data: ', input_data)
(eigen_values, eigen_vectors) = torch.eig(input_data, eigenvectors=True)
print('eigen_values: ', eigen_values)
print('eigen_vectors: ', eigen_vectors)
eigen_values = torch.eig(input_data, eigenvectors=False)
print('eigen_values: ', eigen_values)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.einsum\ntorch.einsum(equation, *operands)\n'
import torch
input_data = torch.randn(2, 3, 4)
print