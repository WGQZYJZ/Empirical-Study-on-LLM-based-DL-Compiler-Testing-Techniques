'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hypot\ntorch.hypot(input, other, *, out=None)\n'
import torch
x = torch.rand(10, 10)
y = torch.rand(10, 10)
print('x: ', x)
print('y: ', y)
print('torch.hypot(x, y): ', torch.hypot(x, y))
print('torch.hypot(x, y).shape: ', torch.hypot(x, y).shape)