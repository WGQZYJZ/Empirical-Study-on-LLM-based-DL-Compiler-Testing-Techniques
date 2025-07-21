'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sqrt\ntorch.sqrt(input, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
x = torch.randn(4)
print('Input data: ', x)
print('Task 3: Call the API torch.sqrt')
print('Output data: ', torch.sqrt(x))