'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dot\ntorch.Tensor.dot(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(2, 3)
other = torch.rand(3, 2)
output = input_tensor.dot(other)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.eig\ntorch.Tensor.eig(_input_tensor, eigenvectors=False)\n'
import torch
input_tensor = torch.rand(2, 2)
(eigenvalues, eigenvectors) = input_tensor.eig(True)
print(eigenvalues)
print(eigenvectors)