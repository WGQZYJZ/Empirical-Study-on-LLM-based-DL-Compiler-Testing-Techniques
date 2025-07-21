'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dot\ntorch.dot(input, other, *, out=None)\n'
import torch
a = torch.randn(4)
b = torch.randn(4)
print('a = ', a)
print('b = ', b)
print('torch.dot(a, b) = ', torch.dot(a, b))
print('a.dot(b) = ', a.dot(b))