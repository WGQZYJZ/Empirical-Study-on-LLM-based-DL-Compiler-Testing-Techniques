'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
import torch
x = torch.rand(3, 3)
print('x: ', x)
y = torch.pow(x, 2)
print('y: ', y)