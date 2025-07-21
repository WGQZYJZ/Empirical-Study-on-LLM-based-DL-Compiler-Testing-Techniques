'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('Input: ', input)
out = torch.special.digamma(input)
print('Output: ', out)