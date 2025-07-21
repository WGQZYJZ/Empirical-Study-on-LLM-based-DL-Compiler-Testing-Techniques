'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
a = torch.randn(4)
print('a =', a)
(b, c) = torch.frexp(a)
print('b =', b)
print('c =', c)