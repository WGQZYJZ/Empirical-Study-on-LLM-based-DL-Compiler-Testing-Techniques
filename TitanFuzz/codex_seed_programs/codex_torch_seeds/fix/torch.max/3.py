'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 5)
print('Input data:')
print(input)
(max_value, max_indices) = torch.max(input, 1)
print('Max values:')
print(max_value)
print('Indices of max values:')
print(max_indices)