'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
input = torch.rand(2, 2, dtype=torch.float)
print('Input: ', input)
output = torch.special.digamma(input)
print('Output: ', output)