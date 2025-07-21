'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
a = torch.randn(1, 3)
print('a: ', a)
b = torch.square(a)
print('b: ', b)
c = torch.pow(a, 2)
print('c: ', c)