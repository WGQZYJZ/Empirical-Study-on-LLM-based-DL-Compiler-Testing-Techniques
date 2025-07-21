'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lgamma\ntorch.lgamma(input, *, out=None)\n'
import torch
x = torch.rand(2, 3)
print('x = ', x)
print('torch.lgamma(x) = ', torch.lgamma(x))
y = torch.rand(2, 3)
print('y = ', y)
print('torch.lgamma(x, out=y) = ', torch.lgamma(x, out=y))
print('y = ', y)