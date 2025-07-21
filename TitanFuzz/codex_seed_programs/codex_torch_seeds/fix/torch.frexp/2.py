'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
x = torch.rand(3, 3)
print('Input data: ', x)
y = torch.frexp(x)
print('Output data: ', y)