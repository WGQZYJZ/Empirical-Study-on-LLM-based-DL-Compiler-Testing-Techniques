'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acos\ntorch.acos(input, *, out=None)\n'
import torch
x = torch.randn(1, 2, 3)
print('Input data: ', x)
out = torch.acos(x)
print('Output data: ', out)