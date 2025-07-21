'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(1, 3)
print('input: ', input)
print('Task 3: Call the API torch.amax')
output = torch.amax(input)
print('output: ', output)