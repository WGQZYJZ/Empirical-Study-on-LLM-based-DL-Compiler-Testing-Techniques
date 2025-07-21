'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, dtype=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(2, 3)
print('input:', input)
print('Task 3: Call the API torch.mean')
output = torch.mean(input, dim=0)
print('output:', output)