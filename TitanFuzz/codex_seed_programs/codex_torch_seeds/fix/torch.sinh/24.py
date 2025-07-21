'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sinh\ntorch.sinh(input, *, out=None)\n'
import torch
import torch
x = torch.randn(4, 4)
print('Input data: ', x)
print('Output data: ', torch.sinh(x))