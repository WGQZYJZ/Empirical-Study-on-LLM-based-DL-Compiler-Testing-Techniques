'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fix\ntorch.fix(input, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input = torch.randn(4, 4)
print('input = ', input)
print('Task 3: Call the API torch.fix')
output = torch.fix(input)
print('output = ', output)