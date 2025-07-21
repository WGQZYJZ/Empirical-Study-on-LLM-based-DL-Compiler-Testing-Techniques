'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_to\ntorch.broadcast_to(input, shape)\n'
import torch
x = torch.arange(1, 3)
print('x =', x)
y = torch.broadcast_to(x, (2, 2))
print('y =', y)
z = torch.broadcast_tensors(x, torch.ones(2, 2))
print('z =', z)