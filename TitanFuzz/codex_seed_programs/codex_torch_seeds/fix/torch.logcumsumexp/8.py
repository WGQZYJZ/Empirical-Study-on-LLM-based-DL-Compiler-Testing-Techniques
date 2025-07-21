'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logcumsumexp\ntorch.logcumsumexp(input, dim, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print('input: \n', input)
print('\nlogcumsumexp: \n', torch.logcumsumexp(input, dim=1))