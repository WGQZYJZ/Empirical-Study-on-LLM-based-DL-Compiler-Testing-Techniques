'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.remainder\ntorch.remainder(input, other, *, out=None)\n'
import torch
x = torch.randn(4)
print('Input data: ', x)
y = torch.remainder(x, 2)
print('Output data: ', y)