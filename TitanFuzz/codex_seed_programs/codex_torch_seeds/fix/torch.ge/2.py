'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ge\ntorch.ge(input, other, *, out=None)\n'
import torch
a = torch.randn(4, 4)
a_ge = torch.ge(a, a)
print('a_ge = ', a_ge)
b = torch.randn(4, 4)
b_ge = torch.ge(a, b)
print('b_ge = ', b_ge)