'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent, *, out=None)\n'
import torch
x = torch.rand(4, 4)
y = torch.pow(x, 2)
print('Input data: \n', x)
print('Output data: \n', y)