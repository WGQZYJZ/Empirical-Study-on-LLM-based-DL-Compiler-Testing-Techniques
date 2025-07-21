'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(1, 4)
print('Input data: ', input)
print('Task 3: Call the API torch.lgamma')
output = torch.lgamma(input)
print('Output data: ', output)