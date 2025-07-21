'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rsqrt\ntorch.rsqrt(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print('Input data: ', x)
y = torch.rsqrt(x)
print('Output data: ', y)