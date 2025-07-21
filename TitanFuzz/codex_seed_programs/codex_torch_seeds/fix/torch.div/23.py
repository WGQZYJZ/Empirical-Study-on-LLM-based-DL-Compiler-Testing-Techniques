'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.div\ntorch.div(input, other, *, rounding_mode=None, out=None)\n'
import torch
x = torch.randn(2, 3, dtype=torch.float)
y = torch.randn(2, 3, dtype=torch.float)
print('x: ', x)
print('y: ', y)
z = torch.div(x, y)
print('z: ', z)