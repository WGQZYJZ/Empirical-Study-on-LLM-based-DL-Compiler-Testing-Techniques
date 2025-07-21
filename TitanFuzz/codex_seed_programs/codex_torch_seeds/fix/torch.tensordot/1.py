'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensordot\ntorch.tensordot(a, b, dims=2, out=None)\n'
import torch
a = torch.arange(1, 17).view(2, 2, 4)
b = torch.arange(1, 17).view(2, 4, 2)
print('a = ', a)
print('b = ', b)
c = torch.tensordot(a, b, dims=2)
print('c = ', c)
print('c.shape = ', c.shape)