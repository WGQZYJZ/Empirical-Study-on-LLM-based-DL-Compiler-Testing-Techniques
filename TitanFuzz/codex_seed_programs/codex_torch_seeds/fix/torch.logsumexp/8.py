'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logsumexp\ntorch.logsumexp(input, dim, keepdim=False, *, out=None)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('PyTorch location: ', torch.__file__)
print('PyTorch path: ', torch.__path__)
print('\nTask 2: Generate input data')
input = torch.randn(3, 4)
print('input: ', input)
print('\nTask 3: Call the API torch.logsumexp')
print('torch.logsumexp(input, dim, keepdim=False, *, out=None)')
dim = 1
keepdim = False
out = torch.logsumexp(input, dim, keepdim, out=None)
print('dim: ', dim)
print('keepdim: ', keepdim)
print('out: ', out)