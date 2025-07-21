'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
x = torch.randn(3, 3)
print('x = ', x)
y = torch.randn(3, 3)
print('y = ', y)
z = torch.dstack([x, y])
print('z = ', z)