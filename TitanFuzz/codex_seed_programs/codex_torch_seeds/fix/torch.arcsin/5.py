'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsin\ntorch.arcsin(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print('Input data: \n', x)
print('ArcSine of input data: \n', torch.arcsin(x))