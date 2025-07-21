'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
import math
input = torch.randn(5, 5)
print('Input: ', input)
output = torch.special.digamma(input)
print('Output: ', output)
output = torch.special.digamma(input, out=input)
print('Output: ', output)
print('Output: ', output.shape)