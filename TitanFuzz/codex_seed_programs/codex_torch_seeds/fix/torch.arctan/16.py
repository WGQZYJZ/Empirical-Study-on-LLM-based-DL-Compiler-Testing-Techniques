'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arctan\ntorch.arctan(input, *, out=None)\n'
import torch
x = torch.randn(1, 3)
print('Input data: ', x)
y = torch.arctan(x)
print('Output data: ', y)