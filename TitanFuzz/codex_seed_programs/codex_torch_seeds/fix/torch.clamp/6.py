'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
x = torch.randn(10)
print('x: ', x)
print('Task 3: Call the API torch.clamp')
y = torch.clamp(x, min=(- 0.5), max=0.5)
print('y: ', y)