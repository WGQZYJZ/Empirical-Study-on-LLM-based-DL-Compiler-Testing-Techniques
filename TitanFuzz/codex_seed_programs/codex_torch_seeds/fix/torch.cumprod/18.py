'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumprod\ntorch.cumprod(input, dim, *, dtype=None, out=None)\n'
import torch
a = torch.randn(4, 4)
print('Input: ', a)
print('Output: ', torch.cumprod(a, dim=0))
print('Output: ', torch.cumprod(a, dim=1))