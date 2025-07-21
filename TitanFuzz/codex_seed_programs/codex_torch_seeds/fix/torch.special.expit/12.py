'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.expit\ntorch.special.expit(input, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
x = torch.randn(1, 2, 3)
print('x = ', x)
print('Task 3: Call the API torch.special.expit')
y = torch.special.expit(x)
print('y = ', y)