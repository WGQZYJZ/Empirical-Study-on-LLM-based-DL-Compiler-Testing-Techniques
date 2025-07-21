'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.digamma\ntorch.digamma(input, *, out=None)\n'
import torch
x = torch.randn(1, 3)
y = torch.digamma(x)
print('The input data:\n', x)
print('The output data:\n', y)