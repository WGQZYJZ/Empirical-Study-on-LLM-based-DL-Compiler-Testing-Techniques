'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
x = torch.randn(2, 3)
print('x: ', x)
y = torch.frexp(x)
print('y: ', y)