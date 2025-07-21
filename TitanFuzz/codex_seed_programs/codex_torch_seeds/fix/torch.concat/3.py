'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.concat\ntorch.concat(tensors, dim=0, *, out=None)\n'
import torch
x1 = torch.randn(3, 3)
x2 = torch.randn(3, 3)
print('x1: ', x1)
print('x2: ', x2)
y = torch.concat([x1, x2], dim=0)
print('y: ', y)