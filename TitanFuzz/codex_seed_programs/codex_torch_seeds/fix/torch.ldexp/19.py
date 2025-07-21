'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ldexp\ntorch.ldexp(input, other, *, out=None)\n'
import torch
a = torch.randn(4, 4)
print('a: ', a)
b = torch.randn(4, 4)
print('b: ', b)
print('torch.ldexp(a, b): ', torch.ldexp(a, b))