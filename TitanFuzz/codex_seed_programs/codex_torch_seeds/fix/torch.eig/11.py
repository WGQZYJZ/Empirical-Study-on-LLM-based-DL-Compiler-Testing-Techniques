'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eig\ntorch.eig(input, eigenvectors=False, *, out=None)\n'
import torch
input = torch.randn(3, 3, requires_grad=True)
print('input: ', input)
(eigen_value, eigen_vector) = torch.eig(input, True)
print('eigen_value: ', eigen_value)
print('eigen_vector: ', eigen_vector)
eigen_value = torch.eig(input, False)
print('eigen_value: ', eigen_value)
'\nTask 4: Call the API torch.eig\ntorch.eig(a, eigenvectors=False, *, out=None)\n'
input = torch.randn(3, 3, requires_grad=True)
print('input: ', input)
(eigen_value, eigen_vector) = torch.eig(input, True)
print('eigen_value: ', eigen_value)
print('eigen_vector: ', eigen_vector)
eigen_value = torch.eig(input, False)
print('eigen_value: ', eigen_value)