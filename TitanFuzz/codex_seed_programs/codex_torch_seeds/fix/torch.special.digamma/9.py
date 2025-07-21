'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
input = torch.randn(5, 5)
output = torch.special.digamma(input)
print('Input: ', input)
print('Output: ', output)