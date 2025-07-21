'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logcumsumexp\ntorch.logcumsumexp(input, dim, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3, 4)
print('input: ', input)
output = torch.logcumsumexp(input, dim=1)
print('output: ', output)