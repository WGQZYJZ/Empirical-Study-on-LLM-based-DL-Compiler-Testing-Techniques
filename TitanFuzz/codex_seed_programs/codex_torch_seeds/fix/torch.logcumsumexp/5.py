'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logcumsumexp\ntorch.logcumsumexp(input, dim, *, out=None)\n'
import torch
input = torch.randn(2, 3)
print('Input:', input)
print('Output:', torch.logcumsumexp(input, dim=1))