'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.digamma\ntorch.digamma(input, *, out=None)\n'
import torch
input = torch.rand(10, 10)
output = torch.digamma(input)
print('output =', output)