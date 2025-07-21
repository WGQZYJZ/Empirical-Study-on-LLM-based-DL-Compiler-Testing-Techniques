'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.negative\ntorch.negative(input, *, out=None)\n'
import torch
x = torch.randn(2, 3)
print('x: ', x)
y = torch.negative(x)
print('y: ', y)
z = torch.neg(x)
print('z: ', z)