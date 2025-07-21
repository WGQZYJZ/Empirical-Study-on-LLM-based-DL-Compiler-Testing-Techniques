'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.digamma\ntorch.special.digamma(input, *, out=None)\n'
import torch
input = torch.rand(1, dtype=torch.float32)
output = torch.special.digamma(input)
print('input: ', input)
print('output: ', output)