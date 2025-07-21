'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input, dim, keepdim=False, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(3, 5)
print(input)
print('Task 3: Call the API torch.max')
(max_value, max_index) = torch.max(input, 1)
print('max_value: ', max_value)
print('max_index: ', max_index)