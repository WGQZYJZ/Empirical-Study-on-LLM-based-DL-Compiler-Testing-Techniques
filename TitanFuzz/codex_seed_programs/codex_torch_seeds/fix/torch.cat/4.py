'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cat\ntorch.cat(tensors, dim=0, *, out=None)\n'
import torch
x = torch.randn(2, 3)
y = torch.randn(2, 3)
print('x = ', x)
print('y = ', y)
z = torch.cat((x, y), dim=0)
print('z = ', z)
z = torch.cat((x, y), dim=1)
print('z = ', z)