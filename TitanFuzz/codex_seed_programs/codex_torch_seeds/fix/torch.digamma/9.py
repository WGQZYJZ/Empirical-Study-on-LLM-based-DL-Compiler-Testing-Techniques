'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.digamma\ntorch.digamma(input, *, out=None)\n'
import torch
input = torch.randn(1, 3)
print('Input data: ', input)
output = torch.digamma(input)
print('Output: ', output)