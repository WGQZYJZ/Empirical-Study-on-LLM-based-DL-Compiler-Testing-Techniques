'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frac\ntorch.frac(input, *, out=None)\n'
import torch
x = torch.randn(4)
print('Input data: ', x)
y = torch.frac(x)
print('Output data: ', y)