'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_and\ntorch.logical_and(input, other, *, out=None)\n'
import torch
x = torch.tensor([True, False, True])
y = torch.tensor([False, False, True])
z = torch.logical_and(x, y)
print('x: ', x)
print('y: ', y)
print('z: ', z)