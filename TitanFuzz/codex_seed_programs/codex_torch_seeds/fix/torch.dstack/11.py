'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
a = torch.rand(2, 3)
b = torch.rand(2, 3)
c = torch.rand(2, 3)
d = torch.rand(2, 3)
print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)
print('dstack:', torch.dstack([a, b, c, d]))