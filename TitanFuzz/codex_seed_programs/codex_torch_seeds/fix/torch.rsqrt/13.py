'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rsqrt\ntorch.rsqrt(input, *, out=None)\n'
import torch
x = torch.rand(1)
print('Input x: ', x)
print('Output y: ', torch.rsqrt(x))