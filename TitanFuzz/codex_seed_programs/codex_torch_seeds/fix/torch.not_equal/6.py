'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.not_equal\ntorch.not_equal(input, other, *, out=None)\n'
import torch
x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.not_equal(x, y)
print('x = ', x)
print('y = ', y)
print('z = ', z)