'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.row_stack\ntorch.row_stack(tensors, *, out=None)\n'
import torch
import torch
x = torch.rand(3, 3)
y = torch.rand(3, 3)
z = torch.row_stack((x, y))
print('x:', x)
print('y:', y)
print('z:', z)